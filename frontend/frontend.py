from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json
import cgi
from os import curdir, sep
from backend import server
import webbrowser
import time

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    # GET sends back a Hello world message
    def do_GET(self):

        if self.path == "/":
            self.path="/frontend/public/index.html"
        elif self.path.startswith("/api/v1/stats/"):
            self._set_headers()
            time_frame = int(self.path.split("/api/v1/stats/", 1)[1])
            stats = server.hit_controller.get_hits(time_frame, True)
            result = {
                'result': stats
            }
            self.wfile.write(json.dumps(result))
            return
        elif self.path.startswith("/api/v1/warnings"):
            self._set_headers()
            warnings = server.monitor.get_warnings()
            result = {
                'result': warnings
            }
            self.wfile.write(json.dumps(result))
            return

        try:
			#Check the file extension required and
			#set the right mime type
			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path)
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return
        except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

class FrontEnd():
    def start(self):
        link = 'localhost'
        port = 8080
        server_address = ('localhost', 8080)
        httpd = HTTPServer(server_address, Server)
        print 'Starting httpd on port %d...' % 8080
        webbrowser.open("http://" + link + ":" + str(port));
        httpd.serve_forever()

import threading
import time
import sys
import random
import string
'''
    This module generates log entrance to populate the file.log
'''

sections = ["messages", "profiles", "audios", "tags", "videos", "news", "friends", "photos", "events"]
methods = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]

class LogGenerator():

    def get_new_line(self):
        rand = random.randrange(10)
        rand2 = random.randrange(9)
        path = '/'
        if rand != 9:
            rand_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            path += sections[rand] + "/" + rand_string
        method = methods[rand2]
        date = time.strftime("%d/%b/%Y:%H:%M:%S %z", time.localtime())
        log = '127.0.0.1 user-identifier flavio [%s] "%s %s HTTP/1.0" 200 2326\n' % (date, method, path)
        return log

    def generate(self):
        while True:
            f = open('file.log', 'ab')
            # f.seek(-2, 2)
            # if f.read(2) == '\n\n':
            #    f.seek(-1, 1)
            f.write(self.get_new_line())
            f.close()
            time.sleep(0.001)

def init():
    print 'Argument List:', str(sys.argv)

    if sys.argv == None or len(sys.argv) < 2 or sys.argv[1] == None:
        print "Error: no log file passed on the arguments. E.g. python log/loggenerator.py /usr/flavio/file.log"
        return

    gen = LogGenerator()
    gen.generate();

init()

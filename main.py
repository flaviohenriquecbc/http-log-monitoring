#!/usr/bin/python

from backend import server
from frontend.frontend import FrontEnd
from agent.collector import Collector
import time
import constants
import threading
from backend.monitor import Monitor

import sys

def start_monitor():
    server.monitor.monitor_init()

def start_frontend():
    frontend = FrontEnd()
    frontend.start()

def start_server():
    #start server (monitor and hit_controller)
    server.init()
    start_frontend()

def start_client_agent(file_name):
    print file_name
    # start collector
    collector = Collector(file_name)
    collector.start()

'''
Monitor the stored data and check if any of the conditions were triggered
'''
def monitor_http_request():

    print 'Argument List:', str(sys.argv)

    if sys.argv == None or len(sys.argv) < 2 or sys.argv[1] == None:
        print "Error: no log file passed on the arguments. E.g. python main.py /usr/flavio/file.log"
        return

    # starts the server (backend and frontend)
    p1 = threading.Thread(target=start_server)
    p1.start()

    # starts the agent on the client machine
    # sys.argv[1] - path of the log file
    p2 = threading.Thread(target=start_client_agent, args=(sys.argv[1],))
    p2.start()

    # starts the monitor of the server
    p3 = threading.Thread(target=start_monitor)
    p3.start()


monitor_http_request()

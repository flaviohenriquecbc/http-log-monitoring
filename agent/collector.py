from agent.parser import Parser
import time
import constants
from backend import server

'''
    Watch the log file, parse it and store the relevant data
    This module run on any machine that needs to be monitored
'''
class Collector():

    def __init__(self, file_name):
        self.file_name = file_name

    '''
        Get all the modification in the log file and return the line to be parsed
    '''
    def follow(self, file_name):
        print "Open the file: " + file_name
        thefile = open(file_name)
        thefile.seek(0,0)
        while True:
            line = thefile.readline()
            if not line:
                time.sleep(constants.TIME_RECHECK_LOG)
                continue
            yield line

    '''
        This method stored the values in a variables. Improve: agregate for a period of
        time (e.g. 10secs) before sending it and at the server store it on a database
    '''
    def add_metrics(self, register):
        timestamp = register[0]
        section = register[1]

        if timestamp == None:
            return

        if timestamp > time.time():
            print "Warn: There are some logs with timestamp > now."

        # call an agregate function to avoid multiple requests to the server
        # send aggregated data every period of time (e.g. 10secs)
        self.aggregate(section, timestamp)

    def aggregate(self, section, timestamp):

        # should aggregate the data and just send to the server after a period of time (e.g. 10seconds)
        # not implemented for simplification

        # instead of sending to server, for simplification, I keep it in a variable
        server.hit_controller.new_data(section, timestamp)

    '''
        Monitor a log file, parse and store the data, send new data to the monitor
    '''
    def start(self):
        print 'Starting to collect data from logfile (' + self.file_name + ')'
        loglines = self.follow(self.file_name)
        parser = Parser()
        for line in loglines:
            register = parser.parse(line)
            if register != None:
                #store data
                self.add_metrics(register)

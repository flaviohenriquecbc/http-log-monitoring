import server
import constants
import time

class Monitor():

    def __init__(self):
        self.last_warn_shown = None
        self.warnings = []

    # this method monitors the data and check if something need to be done
    def check(self):
        return self.check_hits()

    # this methods check if the section was hitted more than WARN_AVG_HITS, if so show warn
    def check_hits(self):

        #total hits on the last TIME_MONITOR_HITS (2 minutes)
        total = server.hit_controller.total_hits_overall(constants.TIME_MONITOR_HITS)

        #average of hits (average = total hits / total time shares)
        average = float(total) / (constants.TIME_MONITOR_HITS / constants.BUCKET_TIME_SIZE)
        message_warn = None

        if (self.last_warn_shown == None and average > constants.WARN_AVG_HITS):
            #set flag to know that the message was shown already
            self.last_warn_shown = time.localtime()

            time_at = time.strftime("%d/%b/%Y %H:%M:%S", self.last_warn_shown)
            message_warn = "High traffic generated an alert - hits = %s, triggered at %s" % (total, time_at)
            # print message_warn

            #log on a file this message
            self.store(message_warn)

        elif (self.last_warn_shown != None and average < constants.WARN_AVG_HITS):
            #set flag to know that the message was shown already
            self.last_warn_shown = None

            time_at = time.strftime("%d/%b/%Y %H:%M:%S", time.localtime())
            message_warn = "Normal traffic recovered - hits = %s, triggered at %s" % (total, time_at)
            # print message_warn

            #log on a file this message
            self.store(message_warn)

    def get_warnings(self):
        return self.warnings

    def store(self, message):
        self.warnings.append(message)
        # store warnings on db
        # for simplification, not implemented

    def monitor_init(self):
        while True:
            time.sleep(constants.TIME_MONITOR_HITS)
            self.check()

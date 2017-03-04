import constants
import time
import server
import json

'''
    This module runs on the server to receive and send data about the links accessed
'''
class HitController():

    def __init__(self):
        self.hits = {}
        self.hits_all = {}

    '''
        The hits are received from all the client agents (collectors)
        The hits are agregated in time buckets of BUCKET_TIME_SIZE seconds.
        The timestamp of the bucket is the first second of that bucket
    '''
    def new_data(self, section, timestamp):
        # increment statistic of all history
        if section == None:
            section = '/'

        if section in self.hits_all:
            self.hits_all[section] += 1
        else:
            self.hits_all[section] = 1

        # increment statistic from the last TIME_MONITOR_HITS seconds
        number_time_buckets = constants.TIME_MONITOR_HITS / constants.BUCKET_TIME_SIZE
        timestamp_initial = timestamp - (timestamp % constants.BUCKET_TIME_SIZE)
        idx = timestamp_initial % number_time_buckets

        if not section in self.hits:
            self.hits[section] = [(0, 0)] * number_time_buckets

        time_init, hit = self.hits[section][idx]

        if time_init != timestamp_initial:
            self.hits[section][idx] = timestamp_initial, 1
        else:
            self.hits[section][idx] = time_init, hit + 1

    def get_hits(self, last_seconds, ignore_root_element):
        if last_seconds == -1:
            hits_all = self.hits_all
            #ignore root element on the screen
            if ignore_root_element and '/' in hits_all:
                del hits_all['/']

            return hits_all
        elif last_seconds > constants.TIME_MONITOR_HITS:
            return {}
        else:
            # get the stats from the last_seconds
            min_timestamp = time.time() - last_seconds
            timestamp_initial = min_timestamp - (min_timestamp % constants.BUCKET_TIME_SIZE)
            hits = {}

            for section in self.hits:

                #ignore root element on the screen
                if ignore_root_element and section == '/':
                    continue

                nr_hits = 0
                for i in xrange(0, len(self.hits[section])):
                    time_init, hit = self.hits[section][i]
                    if timestamp_initial - time_init < constants.TIME_MONITOR_HITS and time_init - timestamp_initial >= 0:
                        nr_hits += hit
                        hits[section] = nr_hits
            return hits

    def total_hits_overall(self, last_seconds):
        stats = self.get_hits(last_seconds, False)
        total = 0
        #sum total of hits
        for section in stats:
            total += stats[section]
        return total

# Whenever total traffic for the past 2 minutes exceeds
# a certain number on average, add a message saying that
# High traffic generated an alert - hits = {value}, triggered at {time}
WARN_AVG_HITS=10

#time the data must be updated on the screen
TIME_UPDATE_STATS=10

#time the monitor must check the WARN_HITS : 2minutes
TIME_MONITOR_HITS=120

# The size of the bucket that will keep the statistic in seconds
# This value represents how many consecutive seconds are stored in the same variable
BUCKET_TIME_SIZE=10

#time to check if the log has changed
TIME_RECHECK_LOG=0.1

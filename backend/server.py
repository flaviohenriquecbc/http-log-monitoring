from hitcontroller import HitController
from monitor import Monitor

# This hitsCounter is to replace the access to the database.
# An improvement should be to change it for a database access
def init():
    global hit_controller, monitor
    hit_controller = HitController()
    monitor = Monitor()

import unittest
import time
from backend import server

class TestMonitor(unittest.TestCase):

    def test_show_warn(self):
        server.init()
        for i in range(2*60 + 1):
            server.hit_controller.new_data("images", int(time.time()))
        server.monitor.check()
        self.assertTrue(server.monitor.get_warnings()[0].startswith('High traffic generated an alert'))

    def test_no_warn(self):
        server.init()
        for i in range(2*60):
            server.hit_controller.new_data("images", int(time.time()))
        server.monitor.check()
        self.assertEquals(len(server.monitor.get_warnings()), 0)

if __name__ == '__main__':
    unittest.main()

from backend import server
import unittest
import time

class TestHitController(unittest.TestCase):

    def test_new_data(self):
        server.init()
        server.hit_controller.new_data("images", int(time.time()))
        self.assertEqual(server.hit_controller.get_hits(10, True)['images'], 1)
        server.hit_controller.new_data("images", int(time.time()))
        self.assertEqual(server.hit_controller.get_hits(10, True)['images'], 2)

    def test_new_data_different(self):
        server.init()
        server.hit_controller.new_data("images", int(time.time()))
        server.hit_controller.new_data("profiles", int(time.time()))
        self.assertEqual(server.hit_controller.get_hits(10, True)['images'], 1)

    def test_total_hits_overall(self):
        server.init()
        server.hit_controller.new_data("images", int(time.time()))
        server.hit_controller.new_data("profiles", int(time.time()))
        self.assertEqual(server.hit_controller.total_hits_overall(10), 2)

if __name__ == '__main__':
    unittest.main()

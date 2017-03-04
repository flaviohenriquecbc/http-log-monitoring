import unittest
import time
from agent.parser import Parser

class TestParser(unittest.TestCase):

    def test_new_data(self):
        parser = Parser()
        date_str = time.strftime("%d/%b/%Y:%H:%M:%S %z", time.localtime())
        section = '/images/12'
        log = '127.0.0.1 user-identifier flavio [%s] "GET %s HTTP/1.0" 200 2326\n' % (date_str, section)
        result = parser.parse(log)
        self.assertEqual(result[1], 'images')


if __name__ == '__main__':
    unittest.main()

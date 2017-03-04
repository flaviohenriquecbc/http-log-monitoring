import re
import time
from dateutil import parser, tz
from datetime import datetime

class Parser:

    def parse(self, log_line):

        try:
            if log_line == None:
                return None

            regex = re.compile(r'\A(?P<remoteHost>\S+) (?P<rfc931>\S+) (?P<authUser>\S+) \[(?P<date>[^\]]+)\] "(?P<rawRequest>[^"]*)" (?P<status>\d+) (?P<bytes>\S+)' )
            requestformat = re.compile(r'(?P<method>\S+) (?P<request>(\*|/(?P<section>[^/]*)/\S*|/[^/]*)) (?P<protocol>[^ ]+)?')

            if log_line != None:
                parsed_data = re.match(regex, log_line)
            else:
                return None

            if parsed_data != None and parsed_data.group('rawRequest') != None:
                parsed_request = requestformat.match(parsed_data.group('rawRequest'))
            else:
                return None

            timestamp = None
            if parsed_data.group('date') != None:
                td = parser.parse(parsed_data.group('date').replace(':', ' ', 1)) - datetime(1970, 1, 1, tzinfo=tz.tzutc())
                timestamp = (td.microseconds + (td.seconds + td.days * 86400) * 10**6) // 10**6
            section = parsed_request.group('section')

            return (timestamp, section)
        except:
            return None

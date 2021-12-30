import sys

"""Count hits for each file on web site"""

for line in sys.stdin:
    data = line.strip().split(' ')
    ip, identity, username, datetime, tz, method, page, protocol, status, content_size = data
    print("{0}".format(page))

import sys

"""Display the number of hits for each different file on Web site"""

for line in sys.stdin:

    data = line.strip().split(' ')
    ip, identity, username, datetime, tz, method, page, protocol, status, content_size = data

    print(page)

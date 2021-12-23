import sys

"""Count hits for each file on web site"""

for line in sys.stdin:
    data = line.strip().split(' ')

    print("{0}\t{1}".format(data[6], data[0]))

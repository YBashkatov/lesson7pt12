import sys

"""Display the number of hits for each different file on Web site"""

for line in sys.stdin:

    data = line.strip().split(' ')

    print("{0}\t{1}".format(data[6], data[0]))


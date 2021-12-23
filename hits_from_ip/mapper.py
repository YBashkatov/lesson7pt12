import sys

"""Display number of hits from each IP"""

for line in sys.stdin:
    data = line.strip().split(' ')


    print("{0}\t{1}".format(data[0], data[6]))


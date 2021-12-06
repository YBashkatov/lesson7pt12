import sys
import csv



def mapper():
    for line in sys.stdin:
        data = line.strip().split(' ')
        # if len(data) != 9:
        #     continue

        print("{0}\t{1}".format(data[6], data[0]))

mapper()

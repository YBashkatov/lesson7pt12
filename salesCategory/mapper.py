import sys

"""Sum of sales per category"""

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 6:
        continue
    print("{0}\t{1}".format(data[3], data[4]))


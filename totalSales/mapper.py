import sys

"""Count total num of sales and the total sales value from all stores"""

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 6:
        continue
    print("{0}\t{1}".format(data[2], data[4]))



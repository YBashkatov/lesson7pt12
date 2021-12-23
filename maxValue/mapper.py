import sys

"""Find highest individual sale for each separate store"""

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 6:
        continue
    print("{0}\t{1}".format(data[2], data[4]))



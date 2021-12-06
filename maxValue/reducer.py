import sys


def reducer():
    oldKey = None
    maxSale = 0

    for line in sys.stdin:
        data = line.strip().split('\t')

        if len(data) != 2:
            continue
        thisKey, thisSale = data

        if oldKey and oldKey != thisKey:
            print('{}\t{}'.format(oldKey, maxSale))
            maxSale = 0

        oldKey = thisKey
        if maxSale < float(thisSale):
            maxSale = float(thisSale)

    if oldKey != None:
        print('{}\t{}'.format(oldKey, maxSale))


reducer()
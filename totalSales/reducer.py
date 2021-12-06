import sys


def reducer():
    totalSales = 0.0
    countSales = 0


    for line in sys.stdin:
        data = line.strip().split('\t')

        if len(data) != 2:
            continue

        thisKey, thisSale = data
        totalSales += float(thisSale)
        countSales += 1
        #
    #     if oldKey and oldKey != thisKey:
    #         print('{}\t{}'.format(oldKey, totalSales))
    #
    #
    #     oldKey = thisKey
    #     totalSales += float(thisSale)
    #
    # if oldKey != None:
    print('{}\t{}'.format(countSales, totalSales))


reducer()
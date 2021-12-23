import sys

totalSales = 0.0
countSales = 0

for line in sys.stdin:
    data = line.strip().split('\t')

    if len(data) != 2:
        continue

    thisKey, thisSale = data
    totalSales += float(thisSale)
    countSales += 1

print('{}\t{}'.format(countSales, totalSales))



import sys

oldKey = None
countHits = 0

for line in sys.stdin:
    data = line.strip().split('\t')

    if len(data) != 2:
        continue
    thisKey, thisSource = data
    if thisKey == '/':
        continue
    if oldKey and oldKey != thisKey:
        print('{}\t{}'.format(oldKey, countHits))
        countHits = 0

    oldKey = thisKey
    countHits += 1

if oldKey != None:
    print('{}\t{}'.format(oldKey, countHits))





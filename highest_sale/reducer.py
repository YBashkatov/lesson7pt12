import sys

prev_city = None
max_sale = 0

for line in sys.stdin:
    data = line.strip().split('\t')

    if len(data) != 2:
        continue
    city, value = data

    if prev_city and prev_city != city:
        print('{}\t{}'.format(prev_city, max_sale))
        max_sale = 0

    prev_city = city
    if max_sale < float(value):
        max_sale = float(value)

if prev_city:
    print('{}\t{}'.format(prev_city, max_sale))

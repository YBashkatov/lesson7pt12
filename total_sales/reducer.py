import sys

total_sales = 0.0
count_sales = 0

for line in sys.stdin:
    value = line.strip()

    if len(value) != 1:
        continue

    total_sales += float(value)
    count_sales += 1

print('{}\t{}'.format(count_sales, total_sales))

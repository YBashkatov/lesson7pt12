import sys

prev_sale_type = None
total_sales = 0

for line in sys.stdin:
    data = line.strip().split('\t')

    if len(data) != 2:
        continue
    sale_type, value = data

    if prev_sale_type and prev_sale_type != sale_type:
        print('{}\t{}'.format(prev_sale_type, total_sales))
        total_sales = 0

    prev_sale_type = sale_type
    total_sales += float(value)

if prev_sale_type:
    print('{}\t{}'.format(prev_sale_type, total_sales))

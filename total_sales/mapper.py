import sys

"""Count total num of sales and the total sales value from all stores"""

for line in sys.stdin:
    data = line.strip().split('\t')
    sale_date, sale_time, city, sale_type, value, payment_type = data

    if len(data) != 6:
        continue
    print(value)

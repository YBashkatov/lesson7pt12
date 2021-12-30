import sys

"""Sum of sales per category"""

for line in sys.stdin:
    data = line.strip().split('\t')
    sale_date, sale_time, city, sale_type, value, payment_type = data
    if len(data) != 6:
        continue
    print("{0}\t{1}".format(sale_type, value))

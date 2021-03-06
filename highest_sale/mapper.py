import sys

"""Find highest individual sale for each separate store"""

for line in sys.stdin:
    data = line.strip().split('\t')
    sale_date, sale_time, city, sale_type, value, payment_type = data

    if len(data) != 6:
        continue
    print("{0}\t{1}".format(city, value))

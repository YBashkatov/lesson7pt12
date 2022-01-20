import sys

prev_page = None
count_hits = 0

for line in sys.stdin:
    this_page = line.strip()

    if len(this_page) != 1:
        continue

    if prev_page and prev_page != this_page:
        print('{}\t{}'.format(prev_page, count_hits))
        countHits = 0

    prev_page = this_page
    count_hits += 1

if prev_page:
    print('{}\t{}'.format(prev_page, count_hits))





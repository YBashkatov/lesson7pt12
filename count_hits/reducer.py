import sys

prev_page = None
count_hits = 0

for line in sys.stdin:
    page = line.strip()

    if page == '/':
        continue
    if prev_page and prev_page != page:
        print('{}\t{}'.format(prev_page, count_hits))
        count_hits = 0

    prev_page = page
    count_hits += 1

if prev_page:
    print('{}\t{}'.format(prev_page, count_hits))

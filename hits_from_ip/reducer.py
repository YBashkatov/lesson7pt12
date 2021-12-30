import sys

prev_ip = None
count_hits = 0

for line in sys.stdin:
    data = line.strip()

    if len(data) != 1:
        continue
    ip = data
    if prev_ip and prev_ip != ip:
        print('{}\t{}'.format(prev_ip, count_hits))
        countHits = 0

    prev_ip = ip
    count_hits += 1

if prev_ip:
    print('{}\t{}'.format(prev_ip, count_hits))

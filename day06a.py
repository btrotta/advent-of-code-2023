from utilities import *

arr = parse_single_string()
times = [int(x) for x in arr[0].split(":")[1].strip().split(" ") if x != ""]
distances = [int(x) for x in arr[1].split(":")[1].strip().split(" ") if x != ""]

num_ways = []
for i in range(len(times)):
    n = 0
    time = times[i]
    for t in range(time):
        rem_time = time - t
        dist = rem_time * t
        if dist > distances[i]:
            n += 1
    num_ways.append(n)

ans = 1
for d in num_ways:
    ans *= d
print(ans)

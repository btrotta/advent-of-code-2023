from utilities import *

arr = parse_single_string()

dirs = list(arr[0])

edges = {}
for line in arr[2:]:
    node = line[:3]
    left = line[7:10]
    right = line[12:15]
    edges[node] = [left, right]

steps = 0
node = "AAA"
while node != "ZZZ":
    curr_dir = dirs[steps % len(dirs)]
    if curr_dir == "L":
        node = edges[node][0]
    else:
        node = edges[node][1]
    steps += 1

print(steps)

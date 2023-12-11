from utilities import *
import math

arr = parse_single_string()
arr = [list(a) for a in arr]

# find S
ch = None
for r, a in enumerate(arr):
    for c, ch in enumerate(a):
        if ch == "S":
            break
    if ch == "S":
        break

j = complex(0, 1)

allowed_directions = {"-": {j, -j},
                      "|": {1, -1},
                      "L": {-1, j},
                      "J": {-1, -j},
                      "F": {1, j},
                      "7": {1, -j},
                      "S": {1, -1, j, -j}}

allowed_next_char = {j: {"-", "J", "7"},
                     -j: {"-", "L", "F"},
                     1: {"|", "L", "J"},
                     -1: {"|", "F", "7"}}

start = complex(r, c)
diffs = [-1, 1, -j, j]
visited = {start}
visited_list = [start]
curr = start
curr_arr = arr[int(start.real)][int(start.imag)]
dist = 0
while True:
    for d in diffs:
        next = curr + d
        invalid = ((next.real < 0) or (next.real > len(arr) - 1) or
                   (next.imag < 0) or (next.imag > len(arr[0]) - 1) or
                   (next in visited))
        if invalid:
            continue
        next_arr = arr[int(next.real)][int(next.imag)]
        if (d in allowed_directions[curr_arr]) and (next_arr in allowed_next_char[d]):
            visited.add(next)
            visited_list.append(next)
            curr_arr = next_arr
            curr = next
            break
    else:
        break


max_dist = math.ceil((len(visited_list) - 1) / 2)
print(max_dist)

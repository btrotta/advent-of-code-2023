from utilities import *

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


n_rows = len(arr)
n_cols = len(arr[0])


def is_valid(x):
    if (x.real < 0) or (x.real >= n_rows):
        return False
    if (x.imag < 0) or (x.imag >= n_rows):
        return False
    return True


# replace start character with a pipe shape character
left = start - j
left_char = arr[int(left.real)][int(left.imag)] if is_valid(left) and left in visited else None
right = start + j
right_char = arr[int(right.real)][int(right.imag)] if is_valid(right) and right in visited else None
up = start - 1
up_char = arr[int(up.real)][int(up.imag)] if is_valid(up) and up in visited else None
down = start + 1
down_char = arr[int(down.real)][int(down.imag)] if is_valid(down) and down in visited else None
if ((left_char == "-") and (right_char in ["J", "7", "-"])) or ((right_char == "-") and (left_char in ["L", "F", "7"])):
    arr[int(start.real)][int(start.imag)] = "-"
elif ((up_char == "|") and (down_char in ["J", "L", "|"])) or ((down_char == "|") and (up_char in ["F", "7"])):
    arr[int(start.real)][int(start.imag)] = "|"
elif (right_char in ["-", "J", "7"]) and (down_char in ["|", "J", "L"]):
    arr[int(start.real)][int(start.imag)] = "F"
elif (left_char in ["-", "L", "F"]) and (up_char in ["|", "F", "7"]):
    arr[int(start.real)][int(start.imag)] = "J"
elif (right_char in ["-", "J", "7"]) and (up_char in ["|", "F", "7"]):
    arr[int(start.real)][int(start.imag)] = "L"
elif (left_char in ["-", "L", "F"]) and (down_char in ["|", "J", "L"]):
    arr[int(start.real)][int(start.imag)] = "7"


# iterate over rows and columns, count number of vertical boundaries in each row
edges = {}
num_inside = 0
for r in range(n_rows):
    inside = False
    last_corner = None
    for c in range(n_cols):
        curr = complex(r, c)
        if curr in visited:
            curr_arr = arr[r][c]
            if curr_arr == "|":
                inside = ~inside
            elif curr_arr in ["F", "L"]:
                last_corner = curr_arr
            elif curr_arr in ["J", "7"]:
                if (last_corner == "F") and (curr_arr == "J"):
                    inside = ~inside
                elif (last_corner == "L") and (curr_arr == "7"):
                    inside = ~inside
                last_corner = curr_arr
        else:
            if inside:
                num_inside += 1

print(num_inside)

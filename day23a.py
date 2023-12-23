from utilities import *

arr = parse_single_string()
arr = [list(x) for x in arr]


n_rows = len(arr)
n_cols = len(arr[0])

for i, ch in enumerate(arr[0]):
    if ch == ".":
        start = (0, i)
        break
for i, ch in enumerate(arr[n_rows - 1]):
    if ch == ".":
        end = (n_rows - 1, i)
        break

dist = 0
paths = [[start]]
max_dist = 0
valid_paths = []
while len(paths) > 0:
    new_paths = []
    for p in paths:
        r, c = p[-1]
        if arr[r][c] == ">":
            neighbours = [(r, c + 1)]
        elif arr[r][c] == "v":
            neighbours = [(r + 1, c)]
        elif arr[r][c] == "<":
            neighbours = [(r, c - 1)]
        elif arr[r][c] == "^":
            neighbours = [(r - 1, c)]
        else:
            neighbours = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r1, c1 in neighbours:
            if (r1, c1) == end:
                valid_paths.append(p)
                max_dist = max(max_dist, len(p))
            else:
                valid_move = valid_coords(r1, c1, n_rows, n_cols) and arr[r1][c1] != "#"
                if valid_move and (r1, c1) not in p:
                    new_paths.append(p + [(r1, c1)])
    paths = new_paths

print(max_dist)

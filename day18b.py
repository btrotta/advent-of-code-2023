from utilities import *
import numpy as np

arr = parse_multi_string(sep=" ")
dirs = ["R", "D", "L", "U"]
arr = [[dirs[int(z[-2:-1])], int(z[2:-2], 16)] for x, _, z in arr]


corner_coords = [[0, 0]]
pos = [0, 0]
for dir, n in arr:
    if dir == "U":
        pos[0] -= n
    elif dir == "R":
        pos[1] += n
    elif dir == "D":
        pos[0] += n
    elif dir == "L":
        pos[1] -= n
    corner_coords.append(tuple(pos))

# need coordinates that are 1 away from the edges to ensure there is space between
# subsequent edges when the border doubles back on itself
r_coords = np.unique([c[0] for c in corner_coords] + [c[0] + 1 for c in corner_coords])
c_coords = np.unique([c[1] for c in corner_coords] + [c[1] + 1 for c in corner_coords])
heights = np.diff(r_coords).astype(np.int64)
widths = np.diff(c_coords).astype(np.int64)
lookup_r = {r: i for i, r in enumerate(r_coords)}
lookup_c = {c: i for i, c in enumerate(c_coords)}
corner_coord_indices = [(lookup_r[r], lookup_c[c]) for (r, c) in corner_coords]

coord_indices = {(lookup_r[0], lookup_c[0])}
pos = [lookup_r[0], lookup_c[0]]
for i in range(1, len(corner_coord_indices)):
    prev, next = corner_coord_indices[i-1:i+1]
    r_diff = next[0] - prev[0]
    c_diff = next[1] - prev[1]
    if r_diff == 0:
        for j in range(abs(c_diff)):
            pos[1] += int(c_diff / abs(c_diff))
            coord_indices.add(tuple(pos))
    else:
        for j in range(abs(r_diff)):
            pos[0] += int(r_diff / abs(r_diff))
            coord_indices.add(tuple(pos))


def get_area(r, c):
    height = heights[r] if (r >= 0 and r < len(heights)) else 1
    width = widths[c] if (c >= 0 and c < len(widths)) else 1
    return height * width


visited = set()
area = 0
to_visit = [(-1, -1)]
while len(to_visit) > 0:
    r, c = to_visit.pop()
    if (r, c) in visited:
        continue
    visited.add((r, c))
    area += get_area(r, c)
    for r1, c1 in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        valid_coord = r1 >= -1 and r1 <= len(r_coords) and c1 >= -1 and c1 <= len(c_coords)
        if valid_coord and (r1, c1) not in coord_indices and (r1, c1) not in visited:
            to_visit.append((r1, c1))

ans = (np.sum(heights) + 3) * (np.sum(widths) + 3) - area
print(ans)

from utilities import *
from collections import defaultdict

arr = parse_single_string()
for i, line in enumerate(arr):
    left, right = line.split("~")
    left = [int(x) for x in left.split(",")]
    right = [int(x) for x in right.split(",")]
    arr[i] = [left, right]

bricks = sorted(arr, key=lambda x: x[0][2])

filled_map = {}  # map location to id of brick it is filled with
filled = set()
bricks_below = defaultdict(lambda: set())  # map each brick to set of bricks supporting it
bricks_above = defaultdict(lambda: set())  # map each brick to set of bricks it supports
for i, brick in enumerate(bricks):
    xy_coords = set()
    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            xy_coords.add((x, y))
    curr_z = brick[0][2]
    new_z = curr_z
    for z in range(curr_z - 1, 0, -1):
        new_coords = set([(a, b, z) for a, b in xy_coords])
        if len(set.intersection(new_coords, filled)) == 0:
            new_z = z
        else:
            break
    height = brick[1][2] - brick[0][2]
    bricks[i][0][2] = new_z
    bricks[i][1][2] = new_z + height
    coords = set([(a, b, c) for a, b in xy_coords for c in range(new_z, new_z + height + 1)])
    filled = set.union(coords, filled)
    for c in coords:
        filled_map[c] = i

# get set of bricks above/below
for i, brick in enumerate(bricks):
    lowest_edge = brick[0][2]
    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            below = (x, y, lowest_edge - 1)
            lower_brick = filled_map.get(below)
            if lower_brick is not None:
                bricks_below[i].add(lower_brick)
                bricks_above[lower_brick].add(i)

ans = 0
falling_bricks = {}
for i in range(len(bricks)):
    to_visit = [i]
    falling_bricks[i] = {i}
    while to_visit:
        curr = to_visit.pop()
        for above in bricks_above[curr]:
            if len(set.difference(bricks_below[above], falling_bricks[i])) == 0:
                falling_bricks[i].add(above)
                to_visit.append(above)
    ans += len(falling_bricks[i]) - 1
print(ans)

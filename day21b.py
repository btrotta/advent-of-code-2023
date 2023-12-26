from functools import cache
from utilities import *
from collections import deque


arr = parse_single_string()
arr = [list(x) for x in arr]


def gets(arr):
    n_rows = len(arr)
    n_cols = len(arr[0])
    for r in range(n_rows):
        for c in range(n_cols):
            if arr[r][c] == "S":
                arr[r][c] = "."
                return (r, c)


start = gets(arr)
n_rows = len(arr)
n_cols = len(arr[0])


def shortest_path_from_source(source):
    distances = {source: 0}
    to_visit = deque([source])
    max_dist = 0
    while len(to_visit) > 0:
        (r, c) = to_visit.popleft()
        dist = distances[r, c]
        neighbours = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r1, c1 in neighbours:
            valid_move = valid_coords(r1, c1, n_rows, n_cols) and arr[r1][c1] != "#"
            if valid_move and (r1, c1) not in distances:
                to_visit.append((r1, c1))
                distances[r1, c1] = dist + 1
                max_dist = max(max_dist, dist + 1)
    return distances, max_dist


# distance from corners or start to any square
distances_to_centre, max_dist_from_centre = shortest_path_from_source(start)

# The centre row and column are blank, so, given any square which is i repeats
# vertically and j repeats horizontally from the central square, we can move from the
# centre of the centre square to the centre of the  other square in
# (n_rows * i) + (n_cols * j) steps. (Note that n_rows = n_cols). Also, each point  in
# the square has distance at most n_rows from the centre.
target_steps = 26501365
border_dist = int(target_steps / n_rows)
fully_enclosed_dist = border_dist - 1
num_complete_squares = (fully_enclosed_dist + 1) ** 2 + fully_enclosed_dist ** 2
odd_distance = lambda r, c: (r, c) in distances_to_centre and (distances_to_centre[r, c] % 2) == 1
even_distance = lambda r, c: (r, c) in distances_to_centre and (distances_to_centre[r, c] % 2) == 0
points_with_odd_distance = [(r, c) for r in range(n_rows) for c in range(n_cols) if odd_distance(r, c)]
points_with_even_distance = [(r, c) for r in range(n_rows) for c in range(n_cols) if even_distance(r, c)]
if fully_enclosed_dist % 2 == 0:
    squares_with_even_distance = (fully_enclosed_dist + 1) ** 2
else:
    squares_with_even_distance = fully_enclosed_dist ** 2
squares_with_odd_distance = num_complete_squares - squares_with_even_distance
points_in_contained_squares = squares_with_even_distance * len(points_with_odd_distance) + squares_with_odd_distance * len(points_with_even_distance)


def neighbours_mod(src, offsets):
    # neighbours of (r, c) coord of square (v, h)
    r, c = src
    v, h = offsets
    coords = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    neighbours = []
    for r1, c1 in coords:
        r1_mod, c1_mod = r1 % n_rows, c1 % n_cols
        if arr[r1_mod][c1_mod] == "#":
            continue
        v1, h1 = v, h
        if r1 < 0:
            v1 = v - 1
        elif r1 > n_rows - 1:
            v1 = v + 1
        if c1 < 0:
            h1 = h - 1
        elif c1 > n_cols - 1:
            h1 = h + 1
        neighbours.append(((r1_mod, c1_mod), (v1, h1)))
    return neighbours


def count_reachable(src, dist_to_src, constraint):
    reachable = set()
    distances = {(src, (0, 0)): dist_to_src}
    to_visit = deque([(src, (0, 0))])
    max_dist = target_steps
    while to_visit:
        curr = to_visit.popleft()
        curr_dist = distances[curr]
        if curr_dist == max_dist:
            continue
        for n in neighbours_mod(*curr):
            _, (v, h) = n
            if n not in distances:
                total_dist = curr_dist + 1
                distances[n] = total_dist
                to_visit.append(n)
                if constraint(v, h) and total_dist % 2 == 1:
                    reachable.add(n)
    return reachable, len(reachable)


# Reachable points above north square
r, squares_to_north = count_reachable((0, start[1]), fully_enclosed_dist * n_rows + n_rows // 2, lambda v, h: v < 0)

# Reachable points below south square
r, squares_to_south = count_reachable((n_rows - 1, start[1]), fully_enclosed_dist * n_rows + n_rows // 2, lambda v, h: v > 0)

# Reachable points right of east square
_, squares_to_east = count_reachable((start[0], n_cols - 1), fully_enclosed_dist * n_rows + n_rows // 2, lambda v, h: h > 0 and v == 0)

# Reachable points left of west square
_, squares_to_west = count_reachable((start[0], 0), fully_enclosed_dist * n_rows + n_rows // 2, lambda v, h: h < 0 and v == 0)

# Reachable points on north-east edge
_, squares_one_row = count_reachable((0, n_cols - 1), fully_enclosed_dist * n_rows - 1, lambda v, h: h > 0 and v == -1)
squares_northeast = fully_enclosed_dist * squares_one_row

# Reachable points on south-east edge
_, squares_one_row = count_reachable((n_rows - 1, n_cols - 1), fully_enclosed_dist * n_rows - 1, lambda v, h: h > 0 and v == 1)
squares_southeast = fully_enclosed_dist * squares_one_row

# Reachable points on south-west edge
_, squares_one_row = count_reachable((n_rows - 1, 0), fully_enclosed_dist * n_rows - 1, lambda v, h: h < 0 and v == 1)
squares_southwest = fully_enclosed_dist * squares_one_row


# Reachable points on north-west edge
_, squares_one_row = count_reachable((0, 0), fully_enclosed_dist * n_rows - 1, lambda v, h: h < 0 and v == -1)
squares_northwest = fully_enclosed_dist * squares_one_row

total = points_in_contained_squares + squares_to_north + squares_to_south + squares_to_east + squares_to_west + squares_northwest + squares_southwest + squares_northeast + squares_southeast
print(total)


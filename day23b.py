from utilities import *
from collections import deque

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

edges = defaultdict(lambda : [])
for r in range(n_rows):
    for c in range(n_cols):
        if arr[r][c] == "#":
            continue
        neighbours = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for r1, c1 in neighbours:
            if valid_coords(r1, c1, n_rows, n_cols) and arr[r1][c1] != "#":
                edges[r, c].append((r1, c1))

new_edges = {}
for key, val in edges.items():
    if len(val) == 2:
        continue
    distances = {key: 0}
    to_visit = [key]
    curr_dist = 0
    visited = set()
    new_edges[key] = {}
    while to_visit:
        new_to_visit = []
        for curr in to_visit:
            visited.add(curr)
            for n in edges[curr]:
                if (len(edges[n]) > 2 or n in [start, end]) and (n != key):
                    new_edges[key][n] = curr_dist + 1
                elif n not in visited:
                    new_to_visit.append(n)
        curr_dist += 1
        to_visit = new_to_visit


paths = [(start, )]
path_sets = [{start}]
path_distances = [0]
max_distance_by_path = {((start, ), start): 0}  # map set of vertices and endpoint to max distance
max_dist = 0
count = 0
while len(paths) > 0:
    new_paths = []
    new_distances = []
    for p in paths:
        r, c = p[-1]
        curr_dist = max_distance_by_path[tuple(sorted(p)), (r, c)]
        for r1, c1 in new_edges[r, c]:
            if (r1, c1) == end:
                max_dist = max(max_dist, curr_dist + new_edges[r, c][r1, c1])
            elif (r1, c1) not in p:
                new_path = p + ((r1, c1), )
                new_tuple = tuple(sorted(new_path))
                new_dist = curr_dist + new_edges[r, c][r1, c1]
                max_dist_this_path = max_distance_by_path.get((new_tuple, (r1, c1)), 0)
                if max_dist_this_path < new_dist:
                    max_distance_by_path[new_tuple, (r1, c1)] = new_dist
                    new_paths.append(new_path)
    paths = new_paths
    count += 1

print(max_dist)

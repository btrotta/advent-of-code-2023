from utilities import *
from itertools import product
from math import lcm

arr = parse_single_string()

dirs = list(arr[0])

edges = {}
for line in arr[2:]:
    node = line[:3]
    left = line[7:10]
    right = line[12:15]
    edges[node] = [left, right]

start_nodes = [node for node in edges if node[-1] == "A"]
valid_path_lengths = []
cycle_lengths = []
for node in start_nodes:
    curr = node
    curr_valid_path_lengths = []
    visited_states = {(curr, 0): 0}
    steps = 0
    while True:
        curr_dir = dirs[steps % len(dirs)]
        if curr_dir == "L":
            next = edges[curr][0]
        else:
            next = edges[curr][1]
        steps += 1
        if (next, steps % len(dirs)) in visited_states:
            cycle_lengths.append(steps - visited_states[next, steps % len(dirs)])
            break
        visited_states[(next, steps % len(dirs))] = steps
        if next[-1] == "Z":
            curr_valid_path_lengths.append(steps)
        curr = next
    valid_path_lengths.append(curr_valid_path_lengths)

dist = lcm(*cycle_lengths)
print(dist)

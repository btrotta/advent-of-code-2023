from utilities import *
import numpy as np
from itertools import chain

arr = parse_single_string(False)

seeds = [int(x) for x in arr[0].split(":")[1].strip().split(" ")]

maps = []
curr_map = None
for line in arr[1:]:
    if (line == "\n") or (line == ""):
        continue
    if line[0].isalpha():
        if curr_map:
            maps.append(curr_map)
        curr_map = []
    else:
        curr_map.append([int(x) for x in line.strip().split(" ")])
maps.append(curr_map)

boundaries = list(chain.from_iterable([[y, y + z] for x, y, z in maps[0]]))
curr_boundaries = []
for map_level in range(len(maps) - 1, 0, -1):
    map = maps[map_level]
    curr_boundaries += list(chain.from_iterable([[y, y + z] for x, y, z in map]))
    prev_map = maps[map_level - 1]
    for i, b in enumerate(curr_boundaries):
        for x, y, z in prev_map:
            if (b >= x) and (b < x + z):
                curr_boundaries[i] = b - (x - y)
boundaries = list(np.sort(np.unique(boundaries + curr_boundaries)))

min_num = None
seed_ranges = [[seeds[i], seeds[i] + seeds[i + 1]] for i in range(0, len(seeds), 2)]
for lower, upper in seed_ranges:
    lower_boundary = np.searchsorted(boundaries, lower, "left")
    upper_boundary = np.searchsorted(boundaries, upper, "left")
    for seed in [lower] + boundaries[lower_boundary: upper_boundary]:
        for map in maps:
            for dest, source, length in map:
                if (seed >= source) and (seed < source + length):
                    seed = dest + seed - source
                    break
        if min_num:
            min_num = min(seed, min_num)
        else:
            min_num = seed

print(min_num)

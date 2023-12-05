from utilities import *

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

min_num = None
for seed in seeds:
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

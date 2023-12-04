from utilities import *

arr = parse_single_string()

num_copies = [1 for i in range(len(arr))]
for i, line in enumerate(arr):
    line = line.split(":")[1]
    left, right = line.split(" | ")
    left = left.strip().split(" ")
    right = right.strip().split(" ")
    matches = 0
    for a in right:
        if a == "":
            continue
        if a in left:
            matches += 1
    for j in range(1, matches + 1):
        num_copies[i + j] += num_copies[i]

print(sum(num_copies))

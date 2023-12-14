from utilities import *

arr = parse_single_string()
arr = [list(x) for x in arr]


def north(arr, curr_pos):
    pos = set()
    n_rows = len(arr)
    for c in range(len(arr[0])):
        first_empty = 0
        for r in range(n_rows):
            if (r, c) in curr_pos:
                pos.add((first_empty, c))
                first_empty += 1
            elif arr[r][c] == "#":
                first_empty = r + 1
    return pos


def south(arr, curr_pos):
    pos = set()
    n_rows = len(arr)
    for c in range(len(arr[0])):
        first_empty = n_rows - 1
        for r in range(n_rows - 1, -1, -1):
            if (r, c) in curr_pos:
                pos.add((first_empty, c))
                first_empty -= 1
            elif arr[r][c] == "#":
                first_empty = r - 1
    return pos


def west(arr, curr_pos):
    pos = set()
    n_cols = len(arr[0])
    for r in range(len(arr)):
        first_empty = 0
        for c in range(n_cols):
            if (r, c) in curr_pos:
                pos.add((r, first_empty))
                first_empty += 1
            elif arr[r][c] == "#":
                first_empty = c + 1
    return pos


def east(arr, curr_pos):
    pos = set()
    n_cols = len(arr[0])
    for r in range(len(arr)):
        first_empty = n_cols - 1
        for c in range(n_cols - 1, -1, -1):
            if (r, c) in curr_pos:
                pos.add((r, first_empty))
                first_empty -= 1
            elif arr[r][c] == "#":
                first_empty = c - 1
    return pos


curr_pos = set()
for r in range(len(arr)):
    for c in range(len(arr[0])):
        if arr[r][c] == "O":
            curr_pos.add((r, c))
i = 0
states = [curr_pos]  # ith element is result after i iterations
dirs = [north, west, south, east]


while True:
    for dir in dirs:
        curr_pos = dir(arr, curr_pos)
    i += 1
    if curr_pos in states:
        prev_pos = states.index(curr_pos)
        break
    states.append(curr_pos)


curr_pos = states[prev_pos]
cycle_length = i - prev_pos
num_remaining = 1000000000 - prev_pos
num_after_cycles = num_remaining % cycle_length
for i in range(num_after_cycles):
    for dir in dirs:
        curr_pos = dir(arr, curr_pos)

ans = 0
for r, c in curr_pos:
    ans += len(arr) - r
print(ans)


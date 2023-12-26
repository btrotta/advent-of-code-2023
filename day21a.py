from utilities import *

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

visited = {start}
to_visit = {start}
for i in range(64):
    new_to_visit = set()
    for r, c in to_visit:
        neighbours = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        visited.add((r, c))
        for r1, c1 in neighbours:
            if valid_coords(r1, c1, n_rows, n_cols) and arr[r1][c1] == ".":
                new_to_visit.add((r1, c1))
    to_visit = new_to_visit

print(len(to_visit))

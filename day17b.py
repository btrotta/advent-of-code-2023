from utilities import *

arr = parse_single_string()
arr = [[int(x) for x in list(line)] for line in arr]

# each node of the graph is a tuple (position, direction), where direction is the
# direction ("v" or "h", vertical or horizontal), moved in to arrive at the node
edges = {}

n_rows = len(arr)
n_cols = len(arr[0])
for r in range(n_rows):
    for c in range(n_cols):
        edges[(r, c), "v"] = {}
        for i in list(range(-10, -3, 1)) + list(range(4, 11, 1)):
            if valid_coords(r, c + i, n_rows, n_cols):
                lower, upper = min(c, c + i), max(c, c + i)
                edges[(r, c), "v"][(r, c + i), "h"] = sum([arr[r][j] for j in range(lower, upper + 1)]) - arr[r][c]
        edges[(r, c), "h"] = {}
        for i in list(range(-10, -3, 1)) + list(range(4, 11, 1)):
            if valid_coords(r + i, c, n_rows, n_cols):
                lower, upper = min(r, r + i), max(r, r + i)
                edges[(r, c), "h"][(r + i, c), "v"] = sum([arr[j][c] for j in range(lower, upper + 1)]) - arr[r][c]

sources = [((0, 0), "v"), ((0, 0), "h")]
dests = [((n_rows - 1, n_cols - 1), "v"), ((n_rows - 1, n_cols - 1), "h")]
min_path = min([shortest_path(edges, src, dest) for src in sources for dest in dests])
print(min_path)

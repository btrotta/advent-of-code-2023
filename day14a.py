from utilities import *

arr = parse_single_string()
arr = [list(x) for x in arr]


ans = 0
n_rows = len(arr)
for c in range(len(arr[0])):
    first_empty = 0
    for r in range(n_rows):
        if arr[r][c] == "O":
            ans += n_rows - first_empty
            first_empty += 1
        elif arr[r][c] == "#":
            first_empty = r + 1


print(ans)

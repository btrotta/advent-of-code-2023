from utilities import *

arr = parse_01(zero_char=".", one_char="#")
arr = np.array(arr)

# expand
new_rows = []
for r in range(arr.shape[0]):
    if arr[r, :].max() == 0:
        for i in range(2):
            new_rows.append(arr[r])
    else:
        new_rows.append(arr[r])
arr = np.vstack(new_rows)
new_cols = []
for c in range(arr.shape[1]):
    if arr[:, c].max() == 0:
        for i in range(2):
            new_cols.append(arr[:, [c]])
    else:
        new_cols.append(arr[:, [c]])
arr = np.hstack(new_cols)

galaxies = list(zip(*np.nonzero(arr)))

sum_dist = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        r1, c1 = galaxies[i]
        r2, c2 = galaxies[j]
        dist = abs(r2 - r1) + abs(c2 - c1)
        sum_dist += dist

print(sum_dist)

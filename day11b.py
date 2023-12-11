from utilities import *

arr = parse_01(zero_char=".", one_char="#")
arr = np.array(arr)

# map original row/col index to expanded row/col index
exp_rows = []
curr_exp_r = 0
for r in range(arr.shape[0]):
    if arr[r, :].max() == 0:
        curr_exp_r += 1000000
    else:
        curr_exp_r += 1
    exp_rows.append(curr_exp_r)
exp_cols = []
curr_exp_c = 0
for c in range(arr.shape[1]):
    if arr[:, c].max() == 0:
        curr_exp_c += 1000000
    else:
        curr_exp_c += 1
    exp_cols.append(curr_exp_c)

galaxies = list(zip(*np.nonzero(arr)))

sum_dist = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        r1, c1 = galaxies[i]
        r2, c2 = galaxies[j]
        dist = abs(exp_rows[r2] - exp_rows[r1]) + abs(exp_cols[c2] - exp_cols[c1])
        sum_dist += dist

print(sum_dist)

from utilities import *
import numpy as np

rows = parse_01()

arrs = []
curr_arr = []
for row in rows:
    if row == []:
        arrs.append(np.array(curr_arr))
        curr_arr = []
    else:
        curr_arr.append(row)
arrs.append(np.array(curr_arr))


def get_reflection(a):
    for r in range(1, len(a)):
        reflected_len = min(r, len(a) - r)
        ref_top = a[r - reflected_len: r, :]
        ref_bottom = a[r: r + reflected_len, :]
        if np.all(ref_top == np.flipud(ref_bottom)):
            return 100 * r
    for c in range(1, len(a[0])):
        reflected_len = min(c, len(a[0]) - c)
        ref_left = a[:, c - reflected_len: c]
        ref_right = a[:, c: c + reflected_len]
        if np.all(ref_left == np.fliplr(ref_right)):
            return c


ans = 0
for a in arrs:
    ans += get_reflection(a)

print(ans)

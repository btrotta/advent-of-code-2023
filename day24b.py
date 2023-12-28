from utilities import *
import numpy as np
from copy import deepcopy

arr = parse_single_string()
for i, line in enumerate(arr):
    left, right = line.split(" @ ")
    pos = [int(x) for x in left.split(", ")]
    vel = [int(x) for x in right.split(", ")]
    arr[i] = [pos, vel]


def det(A):
    ans = 0
    if len(A) == 1:
        return A[0][0]
    for i in range(len(A)):
        for j in range(len(A[0])):
            sub = [[x for m, x in enumerate(a) if m != j] for n, a in enumerate(A) if n != i]
            ans += (-1) ** (i + j) * A[i][j] * det(sub)
    return ans


# Cramer's rule
def cramer(coeffs_arr, y):
    ans = []
    denom = det(coeffs_arr)
    for i in range(6):
        Ai = deepcopy(coeffs_arr)
        for j in range(len(coeffs_arr)):
            Ai[j][i] = y[j][0]
        ans.append(det(Ai) / denom)
    return ans


# based on solution here:
# https://www.reddit.com/r/adventofcode/comments/18pum3b/comment/ker6qsa/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
p, v = arr[0]
coeffs_arr = []
y_arr = []
for i in range(1, 3):
    q, u = arr[i]
    coeffs_arr.append([v[1] - u[1], u[0] - v[0], 0, q[1] - p[1], p[0] - q[0], 0])
    coeffs_arr.append([0, v[2] - u[2], u[1] - v[1], 0, q[2] - p[2], p[1] - q[1]])
    coeffs_arr.append([v[2] - u[2], 0, u[0] - v[0], q[2] - p[2], 0, p[0] - q[0]])
    y_arr.append([p[0] * v[1] - q[0] * u[1] - p[1] * v[0] + q[1] * u[0]])
    y_arr.append([p[1] * v[2] - q[1] * u[2] - p[2] * v[1] + q[2] * u[1]])
    y_arr.append([p[0] * v[2] - q[0] * u[2] - p[2] * v[0] + q[2] * u[0]])

ans = cramer(coeffs_arr, y_arr)
pos = ans[0] + ans[1] + ans[2]
print(pos - np.round(pos))
print(sum(ans[:3]))

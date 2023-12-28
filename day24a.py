from utilities import *

arr = parse_single_string()
for i, line in enumerate(arr):
    left, right = line.split(" @ ")
    pos = [int(x) for x in left.split(", ")]
    vel = [int(x) for x in right.split(", ")]
    arr[i] = [pos, vel]

min_pos = 200000000000000
max_pos = 400000000000000


def single_row_solution(p0, p1, v0, v1):
    # check whether there is a solution to v0 * t0 - v1 * t1 = p1 - p0 for t0, t1 > 0
    p_diff = p1 - p0
    if v0 == 0:
        if v1 == 0:
            return p0 == p1 and (min_pos <= p0 <= max_pos)
        else:
            t1 = -p_diff / v1
            p1 = p1 + v1 * t1
            return t1 > 0 and (min_pos <= p1 <= max_pos)
    else:  # v0 != 0
        if v1 == 0:
            t0 = p_diff / v0
            p0 = p0 + t0 * v0
            return t0 > 0 and (min_pos <= p0 <= max_pos)
        else:
            t0_range = [(max_pos - p0) / v0, (min_pos - p0) / v0]
            t1_range = [(x * v0 - p_diff) / v1 for x in t0_range]
            if max(t0_range) <= 0 or max(t1_range) <= 0:
                return False
            p0_range = [p0 + v0 * x for x in t0_range]
            return min(p0_range) <= max_pos and max(p0_range) >= min_pos


ans = 0
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        pos0, vel0 = np.array(arr[i], dtype=np.float64)
        pos1, vel1 = np.array(arr[j], dtype=np.float64)
        coeffs = np.array([[vel0[0], -vel1[0]], [vel0[1], -vel1[1]]], dtype=np.float64)
        y = np.array([[pos1[0] - pos0[0]], [pos1[1] - pos0[1]]], dtype=np.float64)
        # order rows so rows with leading zeros are at the bottom
        row_order = sorted(list(range(coeffs.shape[0])), key=lambda x: list(-np.abs(coeffs[x])))
        coeffs = coeffs[row_order]
        y = y[row_order]
        if np.all(coeffs[1] == 0):
            if y[1] == 0 and single_row_solution(pos1[0], pos1[1], vel1[0], vel1[1]):
                ans += 1
        else:
            first_nonzero = np.flatnonzero(coeffs[1])[0]
            factor = coeffs[1, first_nonzero] / coeffs[0, first_nonzero]
            coeffs[1, :] = coeffs[1, :] - coeffs[0, :] * factor
            y[1] = y[1] - y[0] * factor
            if np.all(coeffs[1] == 0):
                if y[1] == 0 and single_row_solution(pos1[0], pos1[1], vel1[0], vel1[1]):
                    ans += 1
            else:
                t0, t1 = np.linalg.solve(coeffs, y)
                if min(t0, t1) <= 0:
                    continue
                x = pos0[0] + t0 * vel0[0]
                y = pos0[1] + t0 * vel0[1]
                pos = np.array([x, y])
                if np.all(min_pos <= pos) and np.all(pos <= max_pos):
                    ans += 1

print(ans)

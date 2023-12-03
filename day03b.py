from utilities import *

arr = parse_multi_string(sep="")

ans = 0
n_rows = len(arr)
n_cols = len(arr[0])
for row in range(n_rows):
    for col in range(n_cols):
        ch = arr[row][col]
        if ch == "*":
            adj_nums = []
            for i in [row - 1, row, row + 1]:
                if (i >= 0) and (i < n_rows):
                    n = 0
                    for j in [col - 1, col, col + 1]:
                        if j < n:
                            continue
                        if (j >= 0) and (j < n_cols) and arr[i][j].isdigit():
                            m = j - 1
                            n = j + 1
                            str_num = arr[i][j]
                            while (m >= 0) and arr[i][m].isdigit():
                                str_num = arr[i][m] + str_num
                                m -= 1
                            while (n < n_cols) and arr[i][n].isdigit():
                                str_num = str_num + arr[i][n]
                                n += 1
                            adj_nums.append(int(str_num))
            if len(adj_nums) == 2:
                ans += adj_nums[0] * adj_nums[1]

print(ans)

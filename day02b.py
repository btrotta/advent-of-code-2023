from utilities import *

arr = parse_single_string()


def check_line(line):
    line = line.split(":")[1]
    games = line.split(";")
    ans = [0, 0, 0]
    for g in games:
        pairs = g.split(",")
        for p in pairs:
            num, col = p.strip().split(" ")
            num = int(num)
            if col == "red":
                ans[0] = max(num, ans[0])
            elif col == "green":
                ans[1] = max(num, ans[1])
            else:
                ans[2] = max(num, ans[2])
    return ans[0] * ans[1] * ans[2]


ans = 0
for i, line in enumerate(arr):
    ans += check_line(line)

print(ans)

from utilities import *

arr = parse_single_string()


def check_line(line):
    line = line.split(":")[1]
    games = line.split(";")
    for g in games:
        pairs = g.split(",")
        for p in pairs:
            num, col = p.strip().split(" ")
            num = int(num)
            if (col == "red") and (num > 12):
                return False
            elif (col == "green") and (num > 13):
                return False
            elif num > 14:
                return False
    return True


ans = 0
for i, line in enumerate(arr):
    if check_line(line):
        ans += i + 1

print(ans)
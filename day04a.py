from utilities import *

arr = parse_single_string()

ans = 0
for line in arr:
    num = 0
    line = line.split(":")[1]
    left, right = line.split(" | ")
    left = left.strip().split(" ")
    right = right.strip().split(" ")
    for a in right:
        if a == "":
            continue
        if a in left:
            if num == 0:
                num = 1
            else:
                num *= 2
    ans += num

print(ans)

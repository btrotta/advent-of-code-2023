from utilities import *

arr = parse_multi_string(sep="")

ans = 0
for line in arr:
    for ch in line:
        if ch.isnumeric():
            num = int(ch) * 10
            break
    for ch in reversed(line):
        if ch.isnumeric():
            num += int(ch)
            break
    ans += num

print(ans)

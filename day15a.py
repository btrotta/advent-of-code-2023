from utilities import *

arr = parse_single_string()

arr = arr[0].split(",")
ans = 0
for s in arr:
    curr = 0
    for ch in list(s):
        x = ord(ch)
        curr += x
        curr *= 17
    curr = curr % 256
    ans += curr

print(ans)

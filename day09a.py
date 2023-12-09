from utilities import *
import numpy as np

arr = parse_multi_int()

ans = 0
for x in arr:
    last_element = [x[-1]]
    while np.any(x != 0):
        x = np.diff(x)
        last_element.append(x[-1])
    to_add = 0
    filled = 0
    for a in reversed(last_element):
        filled = a + to_add
        to_add = filled
    ans += filled
print(ans)

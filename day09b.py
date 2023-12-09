from utilities import *
import numpy as np

arr = parse_multi_int()

ans = 0
for x in arr:
    first_element = [x[0]]
    while np.any(x != 0):
        x = np.diff(x)
        first_element.append(x[0])
    to_subtract = 0
    filled = 0
    for a in reversed(first_element):
        filled = a - to_subtract
        to_subtract = filled
    ans += filled
print(ans)

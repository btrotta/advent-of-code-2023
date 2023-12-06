from utilities import *
import math

arr = parse_single_string()
t = int(arr[0].split(":")[1].strip().replace(" ", ""))
d = int(arr[1].split(":")[1].strip().replace(" ", ""))

# Let s be the number of seconds charging,
# and t and d the existing record race time and distance.
# Then the distance travelled is (t - s) * s
# We want to find values of s where (t - s) * s >= d,
# i.e. -s**2 + s*t - d >= 0,
# i.e. s**2 - s*t + d <= 0
# We can find this range with the quadratic formula.
x0 = (t - math.sqrt(t**2 - (4 * d))) / 2
x1 = (t + math.sqrt(t**2 - (4 * d))) / 2

lower = max(0, np.ceil(x0))
upper = np.floor(x1)

print(int(upper - lower + 1))

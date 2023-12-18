from utilities import *

arr = parse_multi_string(sep=" ")
arr = [[x, int(y)] for x, y, _ in arr]


def move(pos, dir):
    if dir == "U":
        pos[0] -= 1
    elif dir == "R":
        pos[1] += 1
    elif dir == "D":
        pos[0] += 1
    elif dir == "L":
        pos[1] -= 1


coords = {(0, 0)}
pos = [0, 0]
for dir, n in arr:
    for i in range(n):
        move(pos, dir)
        coords.add(tuple(pos))

min_r, max_r = min([c[0] for c in coords]), max([c[0] for c in coords])
min_c, max_c = min([c[1] for c in coords]), max([c[1] for c in coords])

visited = set()
to_visit = [(min_r - 1, min_c - 1)]
while len(to_visit) > 0:
    r, c = to_visit.pop()
    if (r, c) in visited:
        continue
    visited.add((r, c))
    for r1, c1 in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        valid_coord = r1 >= min_r - 1 and r1 <= max_r + 1 and c1 >= min_c -1 and c1 <= max_c + 1
        if valid_coord and (r1, c1) not in coords and (r1, c1) not in visited:
            to_visit.append((r1, c1))

ans = (max_r - min_r + 3) * (max_c - min_c + 3) - len(visited)
print(ans)

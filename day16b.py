from utilities import *


arr = parse_single_string()
arr = [list(line) for line in arr]


def continue_beam(pos, dir):
    r, c = int(pos.real), int(pos.imag)
    ch = arr[r][c]
    if ch == ".":
        return True
    elif ch == "|" and dir in [-1, 1]:
        return True
    elif ch == "-" and dir in [-j, j]:
        return True
    return False


num_rows = len(arr)
num_cols = len(arr[0])
j = complex(0, 1)


def get_energized(start_pos, start_dir):
    beams = [(start_pos, start_dir)]
    energized = set()
    visited_states = set()
    while len(beams) > 0:
        pos, dir = beams.pop()
        if (pos, dir) in visited_states:
            continue
        while valid_coords_complex(pos, num_rows, num_cols) and continue_beam(pos, dir) and (pos, dir) not in visited_states:
            energized.add(pos)
            visited_states.add((pos, dir))
            pos += dir
        if not(valid_coords_complex(pos, num_rows, num_cols)):
            continue
        energized.add(pos)
        visited_states.add((pos, dir))
        r, c = int(pos.real), int(pos.imag)
        ch = arr[r][c]
        if ch == "/":
            if dir == 1:
                dir = -j
            elif dir == -1:
                dir = j
            elif dir == j:
                dir = -1
            elif dir == -j:
                dir = 1
            new_pos = pos + dir
            if valid_coords_complex(new_pos, num_rows, num_cols):
                beams.append((new_pos, dir))
        elif ch == "\\":
            if dir == 1:
                dir = j
            elif dir == -1:
                dir = -j
            elif dir == j:
                dir = 1
            elif dir == -j:
                dir = -1
            new_pos = pos + dir
            if valid_coords_complex(new_pos, num_rows, num_cols):
                beams.append((new_pos, dir))
        elif ch == "|":
            if valid_coords_complex(pos + 1, num_rows, num_cols):
                beams.append((pos + 1, 1))
            if valid_coords_complex(pos - 1, num_rows, num_cols):
                beams.append((pos - 1, -1))
        elif ch == "-":
            if valid_coords_complex(pos + j, num_rows, num_cols):
                beams.append((pos + j, j))
            if valid_coords_complex(pos - j, num_rows, num_cols):
                beams.append((pos - j, -j))

    return len(energized)


start_configs = [(complex(0, c), 1) for c in range(num_cols)] \
                + [(complex(num_rows - 1, c), -1) for c in range(num_cols)] \
                + [(complex(r, 0), j) for r in range(num_rows)] \
                + [(complex(r, num_cols), -j) for r in range(num_rows)]
max_energized = 0
for pos, dir in start_configs:
    max_energized = max(max_energized, get_energized(pos, dir))

print(max_energized)

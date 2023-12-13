from utilities import *


arr = parse_multi_string()
for a in arr:
    symbols = {".": 0, "?": -1, "#": 1}
    a[0] = [symbols[ch] for ch in a[0]]
    a[1] = [int(x) for x in a[1].split(",")]


def check_valid(start_pos, length, symbols, num_groups_remaining):
    for pos in range(start_pos, start_pos + length):
        if symbols[pos] == 0:
            return False
    if (start_pos + length < len(symbols)) and (symbols[start_pos + length]) == 1:
        return False
    if num_groups_remaining == 1:
        for pos in range(start_pos + length + 1, len(symbols)):
            if symbols[pos] == 1:
                return False
    return True


def narrow_range(first_pos, last_pos, symbols):
    new_first_pos = len(symbols) - 1
    for pos in range(first_pos, last_pos + 1):
        if symbols[pos] != 0:
            new_first_pos = pos
            break
    new_last_pos = last_pos
    for pos in range(new_first_pos, last_pos + 1):
        if symbols[pos] == 1:
            new_last_pos = pos
            break
    return new_first_pos, new_last_pos


ans = 0
for symbols, groups in arr:
    # each key of valid_combs is start pos of ith group, and the value is number of
    # valid arrangements of first i groups with the ith in that position
    valid_combs = {}
    for i in range(len(groups)):
        num_damaged_remaining = sum(groups[i:])
        num_groups_remaining = len(groups) - i
        # last_pos is the last position where we can start the next group
        last_pos = len(symbols) - num_damaged_remaining - (num_groups_remaining - 1)
        if last_pos < 0:
            valid_combs = {}
            break
        if i == 0:
            curr_first, curr_last = narrow_range(0, last_pos, symbols)
            new_valid_combs = {pos: 1 for pos in range(curr_first, curr_last + 1) if
                               check_valid(pos, groups[0], symbols, num_groups_remaining)}
        else:
            new_valid_combs = defaultdict(lambda: 0)
            for prev_start in valid_combs:
                curr_first, curr_last = narrow_range(prev_start + groups[i - 1] + 1, last_pos, symbols)
                for pos in range(curr_first, curr_last + 1):
                    if check_valid(pos, groups[i], symbols, num_groups_remaining):
                        new_valid_combs[pos] += valid_combs[prev_start]
        valid_combs = new_valid_combs
    ans += sum(list(valid_combs.values()))

print(ans)

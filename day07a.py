from utilities import *
from collections import Counter

arr = parse_multi_string()

labels = [ch for ch in "AKQJT98765432"]
char_ranks = {ch: i for i, ch in enumerate(labels)}


def strength(hand):
    counts = Counter(hand)
    if len(counts) == 1:
        return 0
    elif (len(counts) == 2) and (counts.most_common(1)[0][1] == 4):
        return 1
    elif (len(counts) == 2) and (counts.most_common(1)[0][1] == 3):
        return 2
    elif (len(counts) == 3) and (counts.most_common(1)[0][1] == 3):
        return 3
    elif len(counts) == 3:
        return 4
    elif len(counts) == 4:
        return 5
    else:
        return 6


for a in arr:
    a[1] = int(a[1])


arr = sorted(arr, key=lambda x: [strength(x[0])] + [char_ranks[a] for a in x[0]], reverse=True)
ans = sum([(i + 1) * x[1] for i, x in enumerate(arr)])
print(ans)

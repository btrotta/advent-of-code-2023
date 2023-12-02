from utilities import *

arr = parse_single_string()

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
rev_words = ["".join(reversed(w)) for w in words]


def find_first(words, line):
    for i, ch in enumerate(line):
        if ch.isnumeric():
            return int(ch)
        else:
            for j, w in enumerate(words):
                if line[i:].startswith(w):
                    return j + 1


ans = 0
for line in arr:
    ans += find_first(words, line) * 10
    rev_line = "".join(reversed(line))
    ans += find_first(rev_words, rev_line)

print(ans)


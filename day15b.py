from utilities import *

arr = parse_single_string()


def hash(chars):
    idx = 0
    for ch in chars:
        x = ord(ch)
        idx += x
        idx *= 17
    idx = idx % 256
    return idx


boxes = [[] for i in range(256)]
arr = arr[0].split(",")
ans = 0
for s in arr:
    if s[-1] == "-":
        label = s[:-1]
        idx = hash(list(label))
        box = boxes[idx]
        for i, (lens, focal) in enumerate(box):
            if lens == label:
                boxes[idx] = box[:i] + box[(i + 1):]
                break
    else:
        label, focal_str = s.split("=")
        focal = int(focal_str)
        idx = hash(list(label))
        box = boxes[idx]
        for i, (box_label, _) in enumerate(box):
            if box_label == label:
                box[i] = (label, focal)
                break
        else:
            boxes[idx].append((label, focal))

ans = 0
for i, box in enumerate(boxes):
    for j, (_, focal) in enumerate(box):
        ans += (i + 1) * (j + 1) * focal
print(ans)

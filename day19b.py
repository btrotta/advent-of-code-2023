from utilities import *
from collections import Counter
from copy import deepcopy

arr = parse_single_string()


class Node:
    def __init__(self, name, val=None, left=None, right=None, test_attr=None, threshold=None):
        self.modify(name, val, left, right, test_attr, threshold)

    def modify(self, name, val=None, left=None, right=None, test_attr=None, threshold=None):
        self.name = name
        self.val = val
        self.left = left
        self.right = right
        self.test_attr = test_attr
        self.threshold = threshold


nodes = {}
workflows = {}
for line in arr:
    if line == "":
        continue
    if line[0] != "{":
        name = line[:line.find("{")]
        line = line[len(name) + 1: -1]
        steps = line.split(",")
        workflows[name] = []
        for i, step in enumerate(steps):
            node_name = f"{name}_{i}"
            if ":" in step:
                left, right = step.split(":")
                arg1 = left[0]
                op = left[1]
                threshold = int(left[2:])
                test_attr = left[0]
                if right in ["A", "R"]:
                    left_child = len(nodes)
                    nodes[len(nodes)] = Node(len(nodes), val=(right == "A"))
                else:
                    left_child = f"{right}_0"
                if i < len(steps) - 2 or steps[i + 1] in ["A", "R"]:
                    right_child = f"{name}_{i + 1}"
                else:  # we must have i < len(steps) - 1 since step contains ":"
                    right_child = f"{steps[i + 1]}_0"
                if op == ">":
                    threshold += 1
                    left_child, right_child = right_child, left_child
                if node_name in nodes:
                    nodes[node_name].modify(node_name, None, left_child, right_child, test_attr, threshold)
                else:
                    nodes[node_name] = Node(node_name, None, left_child, right_child, test_attr, threshold)
            elif step in ["A", "R"]:
                nodes[node_name] = Node(node_name, val=(step == "A"))
            else:
                nodes[f"{step}_0"] = nodes.get(f"{step}_0", Node(f"{step}_0"))

# check that graph is directed
pointers = Counter()
for node in nodes.values():
    if node.left:
        pointers[node.left] += 1
        pointers[node.right] += 1
assert(pointers.most_common(1)[0][1] == 1)

# depth-first search, for each path count number of valid ratings that follow that path
node = nodes["in_0"]
visited = set()
to_visit = [node]
xmas = ["x", "m", "a", "s"]
node.max_vals = {x: 4001 for x in xmas}
node.min_vals = {x: 1 for x in xmas}
ans = 0
while len(to_visit) > 0:
    node = to_visit[-1]
    if node.left in visited and node.right in visited:
        visited.add(node.name)
        to_visit.pop()
    elif node.val is None:
        left_child = nodes[node.left]
        to_visit.append(left_child)
        left_child.min_vals = deepcopy(node.min_vals)
        left_child.max_vals = deepcopy(node.max_vals)
        left_child.max_vals[node.test_attr] = min(left_child.max_vals[node.test_attr],
                                                  node.threshold)
        right_child = nodes[node.right]
        to_visit.append(right_child)
        right_child.min_vals = deepcopy(node.min_vals)
        right_child.min_vals[node.test_attr] = max(right_child.min_vals[node.test_attr],
                                                  node.threshold)
        right_child.max_vals = deepcopy(node.max_vals)
    else:
        to_visit.pop()
        visited.add(node.name)
        if node.val:
            curr = 1
            for x in xmas:
                curr *= node.max_vals[x] - node.min_vals[x]
            ans += curr

print(ans)

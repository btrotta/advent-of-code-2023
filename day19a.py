from utilities import *

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


nodes = {"A_0": Node("A_0", val=True), "R_0": Node("R_0", val=False)}
workflows = {}
ratings = []
for line in arr:
    if line == "":
        continue
    if line[0] == "{":
        line = line[1:-1]
        ratings_dict = {}
        for eqn in line.split(","):
            left, right = eqn.split("=")
            ratings_dict[left] = int(right)
        ratings.append(ratings_dict)
    else:
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


def parse_graph(ratings_dict):
    node = nodes["in_0"]
    while node.val is None:
        if ratings_dict[node.test_attr] < node.threshold:
            node = nodes[node.left]
        else:
            node = nodes[node.right]
    return node.val


ans = 0
for ratings_dict in ratings:
    if parse_graph(ratings_dict):
        ans += sum(ratings_dict.values())
print(ans)

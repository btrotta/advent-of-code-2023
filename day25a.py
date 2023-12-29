from utilities import *
import networkx as nx

arr = parse_single_string()

edges = defaultdict(lambda: [])
for i, line in enumerate(arr):
    left, right = line.split(": ")
    for x in right.split(" "):
        edges[left].append(x)
        edges[x].append(left)


def shortest_path(start, end, excluded):
    to_visit = deque([(start,)])  # paths to visit
    seen = set()
    while to_visit:
        p = to_visit.popleft()
        curr = p[-1]
        for new in edges[curr]:
            if (new not in seen) and ((curr, new) not in excluded) and ((new, curr) not in excluded):
                new_p = p + (new, )
                if new == end:
                    return new_p
                seen.add(new)
                to_visit.append(new_p)
    return None


def should_cut_edge(x, y):
    p = shortest_path(x, y, [(x, y)])
    for i in range(len(p) - 1):
        r, s = p[i], p[i + 1]
        q = shortest_path(x, y, [(x, y), (r, s)])
        for j in range(len(q) - 1):
            u, v = q[j], q[j + 1]
            w = shortest_path(x, y, [(x, y), (r, s), (u, v)])
            if w is None:
                return [(x, y), (r, s), (u, v)]
    return None


edge_set = set()
for key, val in edges.items():
    for x in val:
        if (key, x) not in edge_set:
            edge_set.add((x, key))
edge_list = list(edge_set)

cut_edges = []
for i, (x, y) in enumerate(edge_list):
    if should_cut_edge(x, y) is not None:
        cut_edges = should_cut_edge(x, y)
        break

# remove edges and count connected components
new_edges = {}
for node, neighbours in edges.items():
    new_edges[node] = [n for n in neighbours if (node, n) not in cut_edges and (n, node) not in cut_edges]

cc = connected_components(new_edges)
print(len(cc[0]) * len(cc[1]))

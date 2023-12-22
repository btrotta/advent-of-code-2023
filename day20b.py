from utilities import *
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import math

arr = parse_single_string()

class Node:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.output_nodes = []
        self.inputs = {}
        self.output = False
        self.on = False

    def process_pulse(self, sender_name, pulse, pulse_queue):
        send = False
        if self.type == "broadcaster":
            send = True
        elif self.type == "%":
            if not pulse:
                self.on = not self.on
                self.output = self.on
                send = True
        elif self.type == "&":
            self.inputs[sender_name] = pulse
            if all(self.inputs.values()):
                self.output = False
            else:
                self.output = True
            send = True
        if send:
            for node in self.output_nodes:
                # pulse_type = "high" if self.output else "low"
                # print(f"{self.name}   -{pulse_type}->    {node.name}")
                pulse_queue.append([self.name, node, self.output])


nodes = {}
edges = []
for line in arr:
    left, right = line.split(" -> ")
    if left == "broadcaster":
        name = "broadcaster"
        nodes[name] = Node(name, "broadcaster")
        edges += [[name, x] for x in right.split(", ")]
    else:
        name, node_type = left[1:], left[0]
        nodes[name] = Node(name, node_type)
        edges += [[name, x] for x in right.split(", ")]

for src, dest in edges:
    if dest not in nodes:
        nodes[dest] = Node(dest, "output")
    nodes[src].output_nodes.append(nodes[dest])
    nodes[dest].inputs[src] = False


# draw graph, code from
# https://stackoverflow.com/a/20133763
G = nx.DiGraph()
edge_tuples = [tuple(e) for e in edges]
G.add_edges_from(edge_tuples)
node_colors = []
for n in G.nodes():
    if nodes[n].type == "&":
        node_colors.append("red")
    elif nodes[n].type == "%":
        node_colors.append("blue")
    else:
        node_colors.append("gray")
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, arrows=True)
plt.show()

final_node = "rx"
# final_node has only one input
final_input = list(nodes[final_node].inputs)[0]
# check that all inputs of final_input are inverters
final_input_2 = nodes[final_input].inputs
assert all(nodes[n].type == "&" for n in final_input_2)
assert all(len(nodes[n].inputs) == 1 for n in final_input_2)
final_input_3 = []
for n in final_input_2:
    final_input_3 += nodes[n].inputs

# check the subgraphs formed by taking all predecessors of a node in final_input_3
# (excluding the broadcaster) are all disjoint
subgraphs = {}
for n in final_input_3:
    seen = {n}
    to_visit = [n]
    while to_visit:
        curr = to_visit.pop()
        for prev in nodes[curr].inputs:
            if prev not in seen:
                to_visit.append(prev)
                seen.add(prev)
    subgraphs[n] = seen
assert (set.intersection(*subgraphs.values()) == {"broadcaster"})


def button(output_node):
    pulse_queue = deque([["button", nodes["broadcaster"], False]])
    low_pulse = False
    while len(pulse_queue) > 0:
        sender_name, receiver, pulse = pulse_queue.popleft()
        if sender_name == output_node and pulse == False:
            low_pulse = True
        receiver.process_pulse(sender_name, pulse, pulse_queue)
    return low_pulse


def reset_nodes():
    for n in nodes:
        for key in nodes[n].inputs:
            nodes[n].inputs[key] = False
        nodes[n].on = False
        nodes[n].output = False


# for each subgraph, apart from the broadcaster and final nodes, it contains only
# flip-flops. It has at most 2**n states, where n is its number of flip-flops
# find the cycle length
# describe each state by the dictionary of flip-flop states and the value of the pulse
# sent by the subgraph's final node
cycle_starts = {}
cycle_lengths = {}
low_pulse_sent = {}
for n in subgraphs:
    reset_nodes()
    middle_nodes = [x for x in subgraphs[n] if x not in [n, "broadcaster"]]
    assert(all(nodes[x].type == "%" for x in middle_nodes))
    states = {tuple([False for x in middle_nodes]): 0}
    count = 0
    low_pulse_sent[n] = []
    while True:
        low_pulse = button(n)
        new_state = tuple([nodes[x].on for x in middle_nodes])
        count += 1
        if low_pulse:
            low_pulse_sent[n].append(count)
        if new_state in states:
            start = states[new_state]
            cycle_starts[n] = start
            cycle_lengths[n] = count - start
            break
        states[new_state] = count


assert(all(cycle_starts[x] == 0 for x in cycle_starts))
assert(all(low_pulse_sent[x] == [cycle_lengths[x]] for x in low_pulse_sent))

# The assertions above show that for all subgraphs, after some number of button presses,
# the cycle repeats from the start. Also, All cycles send a low pulse in the final
# button press of each cycle. Theoretically, these could happen at different times
# during the button press, so that they never sync up in such a way that node
# final_input receives all high pulses. But since the question must have a solution,
# the answer must be the lowest common multiple ofthe cycle lengths.
print(math.lcm(*list(cycle_lengths.values())))

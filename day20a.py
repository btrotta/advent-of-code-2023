from utilities import *
from collections import deque

arr = parse_single_string()


class Node:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.output_nodes = []
        self.inputs = {}  # for & nodes
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


def button():
    pulse_queue = deque([["button", nodes["broadcaster"], False]])
    low_count, high_count = 0, 0
    while len(pulse_queue) > 0:
        sender_name, receiver, pulse = pulse_queue.popleft()
        if pulse:
            high_count += 1
        else:
            low_count += 1
        receiver.process_pulse(sender_name, pulse, pulse_queue)
    return (low_count, high_count)


low_count, high_count = 0, 0
for i in range(1000):
    low, high = button()
    low_count += low
    high_count += high
print(low_count * high_count)

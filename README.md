# Theorems-graph
A simple script to represent theorems as a connected graph

The idea is that any proposition can be represented as a node in a graph, and a theorem is a relation that brings from a collection of nodes to another collection of nodes.

## Nodes
Each node is called Statement. It has different properties such as:
- proposition (example: "is a compact set")
- referee (example: "the set A")
- value True or False
- a list of Theorems

## Theorems
The theorems are relations between two list of nodes and propagate a value, referring to a referee. Its properties are:
- name (example: "Axiom of Completeness")
- start, which is a list of nodes
- ending, which is a second list of nodes

## Functionality
When we propagate a value through the nodes, we first assign a value (True or False) to an initial set of nodes
After that each node that we propagate calls all its theorems. Each theorems call a set of ending nodes if the value is true for all start nodes. The ending nodes propagate again the signal.

We can use this technique to prove a theorems or creating new (faster) theorems. In fact, any path between A and B with lenght > 1 is equivalent to a new theorem of lenght 1. Any alternative path between two set of nodes is a proof of a any theorem between the same set of nodes.

This graph can be potentially used to create a system for organize in a much more efficient way theorems and mathematical knowledge.
A much more simple use can be for students to automatically proof an already known theorem given another set of theorems.

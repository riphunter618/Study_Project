import networkx
from networkx.algorithms.flow import shortest_augmenting_path

G = networkx.DiGraph()
G.add_nodes_from(['S', 'A', 'B', 'C', 'D', 'T'])
G.add_edges_from(
    [('S', 'A', {'capacity': 10}), ('S', 'C', {'capacity': 10}), ('A', 'C', {'capacity': 2}), ('A', 'B', {'capacity': 4}),
     ('A', 'D', {'capacity': 8}), ('D', 'B', {'capacity': 6}), ('D', 'T', {'capacity': 10}), ('B', 'T', {'capacity': 10}),
     ('C', 'D', {'capacity': 9})])
flow_value, flow_dict = networkx.maximum_flow(G, 'S', 'T', flow_func=shortest_augmenting_path)
print(flow_value)

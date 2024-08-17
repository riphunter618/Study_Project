import json
from networkx.readwrite import json_graph
import networkx
import matplotlib.pyplot

file1 = open('map.json')
x = json.load(file1)
H = json_graph.adjacency_graph(x)

# print(H.nodes)
# print(H.edges)
G = networkx.Graph(networkx.single_source_shortest_path(H, 0))
networkx.draw_spring(G, with_labels=True)  # this is used to show all the paths from one source node
matplotlib.pyplot.show()
# networkx.shortest_path(H, 0, 421) will give you the shortest path between a source and target node

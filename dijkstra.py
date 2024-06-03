import networkx

G = networkx.Graph()
e = [('a', 'b', 2), ('a', 'c', 4), ('b', 'c', 1), ('b', 'd', 7), ('c', 'e', 3), ('e', 'd', 2), ('e', 'f', 5),
     ('d', 'f', 1)]
G.add_weighted_edges_from(e)
print(networkx.dijkstra_path(G, 'a', 'f'))  # shortest path
print(networkx.dijkstra_path_length(G, 'a', 'd'))  # path length to a specific vertex after relaxing

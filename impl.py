from dji import Graph

g = Graph(1804)
f = open('map.pypgr', 'r')
c = 0
num = 0
lines = f.readlines()
for i in range(0, 1805):
    g.add_vertex_data(i, i)
for j in lines[1814:]:
    x = j.split(' ')
    g.add_edge(int(x[0]), int(x[1]), 1)
distances = g.dijkstra(21)
for i, d in enumerate(distances):
    if not d == float('inf'):
        print(f"Shortest distance from {c} to {g.vertex_data[i]}: {d}")
        num += 1
print(f'number of nodes {c} is connected to is {num}')

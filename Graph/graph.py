import matplotlib.pyplot as plt
import networkx as nx


edgelist = [['A', 'B', 10],
            ['B', 'C', 20],
            ['B', 'D', 30],
            ['D', 'E', 40],
            ['E', 'A', 10],
            ['B', 'E', 10]]


G = nx.Graph()
for edge in edgelist:
    p1, p2, weight = edge
    G.add_edge(p1, p2, weight=weight)


# plt.axis('off')
# plt.style.use('fivethirtyeight')
# plt.rcParams['figure.figsize'] = (20, 15)
nx.draw(G, pos=nx.circular_layout(G), with_labels=True, node_size=400, arrows=True)
# print(nx.shortest_path(G, "A", "E"))
# print(nx.shortest_path_length(G, "A", "E", weight="weight"))
# for x in nx.all_pairs_dijkstra_path(G):
#     print(x)

# nx.draw_networkx(nx.minimum_spanning_tree(G))

plt.show()

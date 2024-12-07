# Rian Papa
import csv
import networkx as nx
import matplotlib.pyplot as plt

def generate_mst(file):
    edges = []

    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            u, v, weight = int(row[0]), int(row[1]), int(row[2])
            edges.append((u, v, weight))

    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    # Create MST
    mst = nx.minimum_spanning_tree(G, algorithm='kruskal')
    pos = nx.spring_layout(G)

    # Sum of edges of MST
    print (sum(weight for u,v,weight in mst.edges(data='weight')))

    # Draw MST
    nx.draw(mst, pos, with_labels=True)
    nx.draw_networkx_edge_labels(mst, pos, edge_labels={(u, v): float(d['weight']) for u, v, d in mst.edges(data=True)})
    plt.show()

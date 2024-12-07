import csv
import networkx as nx
import matplotlib.pyplot as plt

def test_generate_mst():

    # Create a graph
    G = nx.Graph()
    edges = [(0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)]
    G.add_weighted_edges_from(edges)

    pos = nx.spring_layout(G)
    
    # Draw the graph
    nx.draw(G, pos, with_labels=True)
    plt.show()

def generate_mst(file):
    edges = []

    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            u, v, weight = int(row[0]), int(row[1]), int(row[2])
            edges.append((u, v, weight))

    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    # Draw MST
    mst = nx.minimum_spanning_tree(G, algorithm='kruskal')
    pos = nx.spring_layout(G)

    # Sum of edges of MST
    print (sum(weight for u,v,weight in mst.edges(data='weight')))

    nx.draw(mst, pos, with_labels=True)
    #nx.draw_networkx_edge_labels(mst, pos)
    nx.draw_networkx_edge_labels(mst, pos, edge_labels={(u, v): float(d['weight']) for u, v, d in mst.edges(data=True)})
    plt.show()

#test_generate_mst()
generate_mst('assignment4_Tree/test-input02.csv')

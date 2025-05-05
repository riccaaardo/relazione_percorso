import networkx as nx
import matplotlib.colors as mcolors
import random


def generateGraph(n_nodes):
    G = nx.complete_graph(n_nodes)
    # print(len(G.nodes))
    # print(G.edges)
    # print(color_list)
    return G

def generateColors(G):
    colors = list(mcolors.CSS4_COLORS.keys()) # 148 total colors
    n_colors = random.randint(1, len(G.nodes))
    color_list = random.sample(colors, n_colors) 
    return color_list

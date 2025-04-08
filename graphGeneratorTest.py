import networkx as nx
import matplotlib.colors as mcolors
import random
G = nx.complete_graph(4)
print(len(G.nodes))
print(G.edges)

colors = list(mcolors.CSS4_COLORS.keys()) # 148 total colors. What if we have more nodes than colors? 
n_colors = random.randint(1, len(G.nodes))
color_list = random.sample(colors, n_colors) 
print(color_list)
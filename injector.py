
with open('template.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# print(content)

def inject(n_nodes, colors, edges, content=content):
    # Replace the variables in the template file with the provided values
    # could be done with a regex?
    content = content.replace('$N_NODES', str(n_nodes))
    content = content.replace('$COLORS', str(colors))
    content = content.replace('$EDGES', str(edges))
    
    return content


if __name__ == '__main__':
    n_nodes = 5
    colors = ['red', 'blue', 'green']
    edges = [(1, 2), (2, 3), (3, 4)]
    
    result = inject(n_nodes, colors, edges)
    print(result)
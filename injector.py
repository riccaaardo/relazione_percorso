
with open('template.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# print(content)

def inject(n_nodes, colors, edges, content=content):
    # Converti la lista di colori in una stringa senza parentesi
    colors_str = ', '.join(colors)  # Converte ['red', 'blue', 'green'] in 'red, blue, green'
    
    # Converti la lista di archi in una stringa leggibile
    edges_str = '\n'.join([f"({u}, {v})" for u, v in edges])  # Converst [(1, 2), (2, 3)] in '(1, 2)\n (2, 3)'
    
    # Sostituisci i placeholder nel contenuto
    content = content.replace('$N_NODES', str(n_nodes))
    content = content.replace('$COLORS', colors_str)
    content = content.replace('$EDGES', edges_str)
    
    return content

if __name__ == '__main__':
    n_nodes = 5
    colors = ['red', 'blue', 'green']
    edges = [(1, 2), (2, 3), (3, 4)]
    
    result = inject(n_nodes, colors, edges)
    print(result)
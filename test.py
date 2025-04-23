import graphGeneratorTest
import injector
import AiManager
import networkx

def printSeparator():
    for i in range(50):
        print("#", end="")
    print()

if __name__ == '__main__':
    n_nodes = int(input("Enter the number of nodes: "))
    G = graphGeneratorTest.generateGraph(n_nodes)
    colors = graphGeneratorTest.generateColors(G) # could be an input?

    prompt = injector.inject(len(G.nodes), colors, G.edges)

    printSeparator()
    print("YOUR PROMPT")
    printSeparator()
    print(prompt)

    printSeparator()
    print("ANSWER")
    printSeparator()

    response = AiManager.askOllama(prompt)
    print(response.choices[0].message.content)




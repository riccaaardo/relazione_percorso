import graphGeneratorTest
import injector
import AiManager
import networkx
import clingo
import sys
import solver

def printSeparator():
    for i in range(50):
        print("#", end="")
    print()

if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        n_nodes = sys.argv[1]
        n_nodes = int(n_nodes)
    else:
        n_nodes = 5
    
    G = graphGeneratorTest.generateGraph(n_nodes)
    colors = graphGeneratorTest.generateColors(G) # could be an input?

    prompt = injector.inject(len(G.nodes), colors, G.edges)

    print("\n\n")
    printSeparator()
    print("YOUR PROMPT")
    printSeparator()
    print(prompt)

    print("\n\n")
    printSeparator()
    print("LLM ANSWER")
    printSeparator()


    response = AiManager.askOllama(prompt)
    #llm_parse = response.choices[0].message.content
    print(response)

    print("\n\n")
    printSeparator()
    print("CLINGO ANSWER")
    printSeparator()
    col_response = solver.call_clingo(response)
    #print(col_response)
    if not col_response:
        print("graph is not colorable")
    else:
        for x in col_response:
            print(x)
import graphGeneratorTest
import injector
import AiManager
import networkx
import clingo

def printSeparator():
    for i in range(50):
        print("#", end="")
    print()

def call_clingo(facts):
    ctl = clingo.Control()
    ctl.load("colourability.lp")
    ctl.add(facts)
    ctl.ground()

    with ctl.solve(yield_=True) as hnd:
       ans = hnd.get()
       print("Satisfiable?", ans.satisfiable)

       if not ans.satisfiable:
           return []

       model = hnd.model()
       solution = []
       for sym in model.symbols(atoms=True):
           if sym.name == 'colored':
               solution.append(str(sym))

       return solution

if __name__ == '__main__':
    n_nodes = int(input("Enter the number of nodes: "))
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
    print("ANSWER")
    printSeparator()

    response = AiManager.askOllama(prompt)
    llm_parse = response.choices[0].message.content
    print(llm_parse)

    col_response = call_clingo(llm_parse)
    print(col_response)
    if not col_response:
        print("graph is not colorable")
    else:
        for x in col_response:
            print(x)


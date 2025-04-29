import clingo

def call_clingo(facts):
    ctl = clingo.Control()
    ctl.load("colourability.lp") # path to the logic program
    ctl.add(facts) # facts input by the model
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
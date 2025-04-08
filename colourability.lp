% Given a graph with 4 nodes, the following 2 colors: red, blue
% and the following edges composing the graph: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)
% extract information.

color(red).
color(blue).
color(green).

edge(0,1). edge(1,0).
edge(0,2). edge(2,0).
edge(0,3). edge(3,0).
edge(1,2). edge(2,1).
edge(2,3). edge(3,2).

nNodes(4). % Could be calculated, but since it's in the template, I'll keep it

% Node extraction
node(X) :- edge(X, Y).

% Two nodes are adjacent if an edge connects them
% adj(X,Y) :- edge(X,Y). -> Redundant, it's the edge set itself

% I didn't use the disjunction with all the colors (colored(X, red) | colored(X, blue) | ...) 
% because it wouldn't work when the facts are not pre-established but input from outside
colored(X, C) | unColored(X, C) :- node(X), color(C).

% Each node must be colored
% Since from the successive constraint I know that each node is colored just once,
% I simply need to ensure that in the colored set there are exactly nNodes nodes
:- nNodes(K), #count{X: colored(X,C)} < K.

% 1 color per node
:- colored(X, C), colored(X, C1), C != C1.

% Adjacent nodes must have different colors
:- edge(X, Y), colored(X, C), colored(Y, C), X != Y.
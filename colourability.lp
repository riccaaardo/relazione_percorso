% Given a graph with 4 nodes, the following 2 colors: red, blue
% and the following edges that compose the graph: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3),
% extract information.

color(red).
color(blue).
color(green).

edge(0,1). edge(1,0).
edge(0,2). edge(2,0).
edge(0,3). edge(3,0).
edge(1,2). edge(2,1).
edge(2,3). edge(3,2).

nNodes(4). % potrebbe anche essere derivato, ma è previsto nel template, quindi lo tengo

% estraggo i nodi
node(X) :- edge(X, Y).

% due nodi sono adiacenti se un arco li lega
% adj(X,Y) :- edge(X,Y). -> superfluo! restituisce l'insieme degli archi

% genero le soluzioni
colored(X, C) | unColored(X, C) :- node(X), color(C).

% ogni nodo deve essere colorato
% dal momento che il vincolo subito sucessivo mi garantisce che ogni nodo viene
% colorato esattamente una volta, mi basta assicurarmi che appiano nNodes nodi
% nell'insieme colored.
:- nNodes(K), #count{X: colored(X,C)} < K.

% ad ogni nodo deve essere assegnato esattamente 1 colore
:- colored(X, C), colored(X, C1), C != C1.

% se due nodi sono adiacenti devono essere di colori diversi
:- edge(X, Y), colored(X, C), colored(Y, C), X != Y.
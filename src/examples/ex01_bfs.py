from base.vertex import Vertex
from base.graph import UndirectedGraph
from algorithm.bfs import bfs
from algorithm.utils import print_path

def main():
    a, b, c, d, e = Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E")

    g = UndirectedGraph()
    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(b, d)
    g.add_edge(c, e)

    dist, pred, _ = bfs(g, a)

    # imprime caminho de A até E
    path = print_path(pred, a, e)
    if path:
        print("Path A->E:", " -> ".join(str(v.id) for v in path))
    else:
        print("No path from A to E")
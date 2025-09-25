from base.vertex import Vertex
from base.edge import Edge
from base.graph import Graph
from base.graph import UndirectedGraph
from algorithm.connectivity import connected_components_BFS


def main():
    g = UndirectedGraph()
    # Add vertices
    a, b, c, d, e, f = [Vertex(x) for x in "ABCDEF"]
    for v in [a, b, c, d, e, f]:
        g.add_vertex(v)
    
    # Add edges
    g.add_edge(a, b)
    g.add_edge(b, c)
    g.add_edge(d, e)

    # Count components
    num = connected_components_BFS(g)
    print(g)
    print(f"Number of connected components: {num}")


if __name__ == "__main__":
    main()
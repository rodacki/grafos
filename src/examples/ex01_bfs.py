from base.graph import Graph
from algorithm.bfs import bfs

def main() -> None:
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")

    print("Grafo:")
    print(g)
    print("\nBFS a partir de A:")
    print(" -> ".join(bfs(g, "A")))

if __name__ == "__main__":
    main()
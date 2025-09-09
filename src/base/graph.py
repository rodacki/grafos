from typing import Dict, List

class Graph:
    """Grafo simples não direcionado e não ponderado (lista de adjacência)."""

    def __init__(self) -> None:
        self.adj: Dict[str, List[str]] = {}

    def add_vertex(self, v: str) -> None:
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u: str, v: str) -> None:
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    def neighbors(self, v: str) -> List[str]:
        return self.adj.get(v, [])

    def __str__(self) -> str:
        return "\n".join(f"{v}: {n}" for v, n in self.adj.items())
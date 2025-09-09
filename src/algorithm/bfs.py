import math
from collections import deque
from typing import Dict, List, Optional
from base.graph import Graph
from base.vertex import Vertex

def bfs(graph: Graph, start: Vertex):
    """
    Breadth-First Search (CLRS, Cap. 22).

    Args:
        graph (Graph): The graph (directed or undirected).
        start (Vertex): The source vertex.

    Returns:
        dist (Dict[Vertex, int | float]): shortest-path distances from start
        pred (Dict[Vertex, Optional[Vertex]]): predecessors in BFS tree
        order (List[Vertex]): order of discovery
    """

    # Inicialização
    dist: Dict[Vertex, int | float] = {}
    pred: Dict[Vertex, Optional[Vertex]] = {}
    color: Dict[Vertex, str] = {}
    order: List[Vertex] = []

    for u in graph.vertices():
        color[u] = "WHITE"
        dist[u] = math.inf
        pred[u] = None

    color[start] = "GRAY"
    dist[start] = 0
    pred[start] = None

    # Fila
    q: deque[Vertex] = deque([start])

    # Laço principal
    while q:
        u = q.popleft()
        order.append(u)

        for v in graph.adjacent(u).keys():
            if color[v] == "WHITE":
                color[v] = "GRAY"
                dist[v] = dist[u] + 1
                pred[v] = u
                q.append(v)

        color[u] = "BLACK"

    return dist, pred, order
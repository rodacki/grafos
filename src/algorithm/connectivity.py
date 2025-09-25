import math
from collections import deque
from typing import Dict, List, Optional
from base.graph import Graph, Vertex


def connected_components_BFS(graph: Graph) -> int:

    # Inicialização
    dist: Dict[Vertex, int | float] = {}
    pred: Dict[Vertex, Optional[Vertex]] = {}
    color: Dict[Vertex, str] = {}
    order: List[Vertex] = []

    for u in graph.vertices():
        color[u] = "WHITE"
        dist[u] = math.inf
        pred[u] = None

    components = 0
    for u in graph.vertices():
        if color[u] == "WHITE":
            components += 1
            bfs_visit(graph, u, color,dist,pred, order)

    return components

def bfs_visit(graph: Graph, start: Vertex, color:Dict, dist: Dict, pred: Dict, order:List):
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
    return None
    
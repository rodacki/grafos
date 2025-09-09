from collections import deque
from typing import List
from base.graph import Graph

def bfs(graph: Graph, start: str) -> List[str]:
    visited = set([start])
    order: List[str] = []
    q: deque[str] = deque([start])

    while q:
        u = q.popleft()
        order.append(u)
        for v in graph.neighbors(u):
            if v not in visited:
                visited.add(v)
                q.append(v)
    return order
from typing import Dict, Optional, List
from base.vertex import Vertex

def print_path(pred: Dict[Vertex, Optional[Vertex]], s: Vertex, v: Vertex) -> List[Vertex]:
    """
    Reconstructs the path from source s to vertex v using predecessor map.

    Equivalent to PRINT-PATH(G, s, v) in CLRS (Cap. 22).

    Args:
        pred: predecessor dictionary from BFS (or DFS/Dijkstra).
        s: source vertex
        v: target vertex

    Returns:
        List[Vertex]: the path from s to v (inclusive), or empty if not reachable.
    """
    path: List[Vertex] = []

    def recurse(u: Vertex):
        if u == s:
            path.append(s)
        elif pred[u] is None:
            # no path exists
            path.clear()
        else:
            recurse(pred[u])
            path.append(u)

    recurse(v)
    return path
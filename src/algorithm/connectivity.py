import math
from collections import deque
from typing import Dict, List, Optional
from base.graph import Graph, Vertex
from base.enums import Color


def connected_components_BFS(graph: Graph) -> int:
    """Compute the number of connected components in an undirected graph using BFS.

    This algorithm follows the style presented in *Introduction to Algorithms*
    (Cormen, Leiserson, Rivest, Stein – CLRS), where BFS is used to explore
    all vertices reachable from a given source. Each time a new unvisited
    (WHITE) vertex is found, a BFS tree is started, representing a new
    connected component.

    Args:
        graph (Graph): An undirected graph implementing the Graph interface.

    Returns:
        int: The number of connected components in the graph.

    Notes:
        - Original name in Portuguese: **componentes conexas (BFS)**.
        - Uses BFS to explore each component independently.
        - Complexity: O(V + E), where V = number of vertices, E = number of edges.
    """

    # Initialization
    dist: Dict[Vertex, int | float] = {}
    pred: Dict[Vertex, Optional[Vertex]] = {}
    color: Dict[Vertex, str] = {}
    order: List[Vertex] = []

    for u in graph.vertices():
        color[u] = Color.WHITE
        dist[u] = math.inf
        pred[u] = None

    components = 0
    for u in graph.vertices():
        if color[u] == Color.WHITE:
            components += 1
            bfs_visit(graph, u, color,dist,pred, order)

    return components

def bfs_visit(
    graph: Graph,
    start: Vertex,
    color: Dict[Vertex, Color],
    dist: Dict[Vertex, float],
    pred: Dict[Vertex, Optional[Vertex]],
    order: List[Vertex],
) -> None:
    """Perform a BFS traversal from a starting vertex.

    This subroutine explores all vertices reachable from the given `start`
    vertex, updating color, distance, and predecessor information as in the
    CLRS BFS algorithm. It is used internally by `connected_components_BFS`
    to explore one connected component at a time.

    Args:
        graph (Graph): The graph to traverse.
        start (Vertex): The initial vertex for the BFS tree.
        color (Dict[Vertex, Color]): Color state of each vertex
            (WHITE = undiscovered, GRAY = discovered, BLACK = finished).
        dist (Dict[Vertex, float]): Distance from the starting vertex.
        pred (Dict[Vertex, Optional[Vertex]]): Predecessor of each vertex in the BFS tree.
        order (List[Vertex]): List of vertices in the order they were first discovered.

    Returns:
        None

    Notes:
        - Original name in Portuguese: **bfs_visita**.
        - Implements the standard BFS loop with a queue.
        - Called once per connected component.
    """
    color[start] = Color.GRAY
    dist[start] = 0
    pred[start] = None

    # queue
    q: deque[Vertex] = deque([start])

    # Main loop
    while q:
        u = q.popleft()
        order.append(u)

        for v in graph.adjacent(u).keys():
            if color[v] == Color.WHITE:
                color[v] = Color.GRAY
                dist[v] = dist[u] + 1
                pred[v] = u
                q.append(v)

        color[u] = Color.BLACK
    return None
    
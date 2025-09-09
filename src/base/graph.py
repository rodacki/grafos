from __future__ import annotations
from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Iterator, Mapping, MutableMapping

from .vertex import Vertex
from .edge import Edge


class Graph(ABC):
    """
    Abstract base class for graphs represented by an adjacency map.
    """

    def __init__(self) -> None:
        # adjacency: for each u, a dict of neighbors v -> Edge(u,v)
        self._adj: MutableMapping[Vertex, dict[Vertex, Edge]] = defaultdict(dict)

    # ---------------- Common operations ----------------

    def order(self) -> int:
        """
        Returns the number of vertices in the graph.

        Original name in Portuguese: getOrdem()
        """
        return len(self._adj)

    def size(self) -> int:
        """
        Returns the number of edges in the graph.

        Original name in Portuguese: getTamanho()
        """
        return sum(1 for _ in self.edges())

    def vertices(self) -> Iterator[Vertex]:
        """
        Returns an iterator over all vertices in the graph.

        Original name in Portuguese: vertices()
        """
        return iter(self._adj.keys())

    def edges(self) -> Iterator[Edge]:
        """
        Returns an iterator over all edges in the graph.

        Original name in Portuguese: arestas()
        """
        for u, nbrs in self._adj.items():
            for v, e in nbrs.items():
                if self._should_yield_edge(u, v):
                    yield e

    def add_vertex(self, v: Vertex) -> None:
        """
        Adds a vertex to the graph.

        Original name in Portuguese: insereV()
        """
        self._adj.setdefault(v, {})

    def remove_vertex(self, v: Vertex) -> None:
        """
        Removes vertex v and all its incident edges.

        Original name in Portuguese: removeV(v)
        """
        if v not in self._adj:
            return
        for u in list(self._adj.keys()):
            self._adj[u].pop(v, None)
        self._adj.pop(v, None)

    def adjacent(self, v: Vertex) -> Mapping[Vertex, Edge]:
        """
        Returns the adjacency mapping of v (neighbors and corresponding edges).

        Original name in Portuguese: adj(v)
        """
        return self._adj.get(v, {})

    def get_edge(self, u: Vertex, v: Vertex) -> Edge | None:
        """
        Returns the edge (u,v) if it exists, or None otherwise.

        Original name in Portuguese: getA(u,v)
        """
        return self._adj.get(u, {}).get(v)

    def endpoints(self, e: Edge) -> tuple[Vertex, Vertex]:
        """
        Returns the pair of vertices incident to edge e.

        Original name in Portuguese: verticesA(e)
        """
        return (e.u, e.v)

    def opposite(self, v: Vertex, e: Edge) -> Vertex:
        """
        Given a vertex v incident to edge e, returns the opposite vertex.

        Original name in Portuguese: oposto(v,e)
        """
        if e.u == v:
            return e.v
        if e.v == v:
            return e.u
        raise ValueError("Vertex is not incident to the given edge.")

    def __str__(self) -> str:
        """
        Returns a string representation of the graph (adjacency list).

        Original requirement in Portuguese: representação textual do grafo
        """
        lines: list[str] = []
        for u, nbrs in self._adj.items():
            viz = ", ".join(str(v.id) for v in nbrs.keys())
            lines.append(f"{u.id}: [{viz}]")
        return "\n".join(lines)

    # ---------------- Abstract methods ----------------

    @abstractmethod
    def add_edge(self, u: Vertex, v: Vertex,
                 weight: float | None = None, data: object | None = None) -> Edge:
        """Original name in Portuguese: insereA(u,v)"""
        ...

    @abstractmethod
    def remove_edge(self, e: Edge) -> None:
        """Original name in Portuguese: removeA(e)"""
        ...

    @abstractmethod
    def in_degree(self, v: Vertex) -> int:
        """Original name in Portuguese: grauE(v)"""
        ...

    @abstractmethod
    def out_degree(self, v: Vertex) -> int:
        """Original name in Portuguese: grauS(v)"""
        ...

    @abstractmethod
    def degree(self, v: Vertex) -> int:
        """Original name in Portuguese: grau(v)"""
        ...

    @abstractmethod
    def in_edges(self, v: Vertex) -> Iterator[Edge]:
        """Original name in Portuguese: arestasE(v)"""
        ...

    @abstractmethod
    def out_edges(self, v: Vertex) -> Iterator[Edge]:
        """Original name in Portuguese: arestasS(v)"""
        ...

    @abstractmethod
    def _should_yield_edge(self, u: Vertex, v: Vertex) -> bool:
        """
        Internal method: controls whether an edge should be yielded in edges().

        Not in the Portuguese table, but required to avoid duplicates
        in undirected graphs.
        """
        ...


class DirectedGraph(Graph):
    """
    Concrete implementation for directed graphs.
    """

    def add_edge(self, u: Vertex, v: Vertex,
                 weight: float | None = None, data: object | None = None) -> Edge:
        """Original name in Portuguese: insereA(u,v)"""
        self.add_vertex(u)
        self.add_vertex(v)
        e = Edge(u, v, weight=weight, data=data)
        self._adj[u][v] = e
        return e

    def remove_edge(self, e: Edge) -> None:
        """Original name in Portuguese: removeA(e)"""
        self._adj.get(e.u, {}).pop(e.v, None)

    def in_degree(self, v: Vertex) -> int:
        """Original name in Portuguese: grauE(v)"""
        return sum(1 for u in self._adj if v in self._adj[u])

    def out_degree(self, v: Vertex) -> int:
        """Original name in Portuguese: grauS(v)"""
        return len(self._adj.get(v, {}))

    def degree(self, v: Vertex) -> int:
        """
        Returns total degree (in + out).

        Original name in Portuguese: grau(v)
        """
        return self.in_degree(v) + self.out_degree(v)

    def in_edges(self, v: Vertex) -> Iterator[Edge]:
        """Original name in Portuguese: arestasE(v)"""
        for u in self._adj:
            e = self._adj[u].get(v)
            if e is not None:
                yield e

    def out_edges(self, v: Vertex) -> Iterator[Edge]:
        """Original name in Portuguese: arestasS(v)"""
        yield from self._adj.get(v, {}).values()

    def _should_yield_edge(self, u: Vertex, v: Vertex) -> bool:
        return True


class UndirectedGraph(Graph):
    """
    Concrete implementation for undirected graphs.
    """

    def add_edge(self, u: Vertex, v: Vertex,
                 weight: float | None = None, data: object | None = None) -> Edge:
        """Original name in Portuguese: insereA(u,v)"""
        self.add_vertex(u)
        self.add_vertex(v)
        e = Edge(u, v, weight=weight, data=data)
        self._adj[u][v] = e
        # add symmetric copy
        self._adj[v][u] = Edge(v, u, weight=weight, data=data)
        return e

    def remove_edge(self, e: Edge) -> None:
        """Original name in Portuguese: removeA(e)"""
        self._adj.get(e.u, {}).pop(e.v, None)
        self._adj.get(e.v, {}).pop(e.u, None)

    def in_degree(self, v: Vertex) -> int:
        """Original name in Portuguese: grauE(v)"""
        return self.degree(v)

    def out_degree(self, v: Vertex) -> int:
        """Original name in Portuguese: grauS(v)"""
        return self.degree(v)

    def degree(self, v: Vertex) -> int:
        """Original name in Portuguese: grau(v)"""
        return len(self._adj.get(v, {}))

    def in_edges(self, v: Vertex) -> Iterator[Edge]:
        """Original name in Portuguese: arestasE(v)"""
        for u, e in self._adj.get(v, {}).items():
            if self._canonical(v, u):
                yield e

    def out_edges(self, v: Vertex) -> Iterator[Edge]:
        """Original name in Portuguese: arestasS(v)"""
        for u, e in self._adj.get(v, {}).items():
            if self._canonical(v, u):
                yield e

    def _should_yield_edge(self, u: Vertex, v: Vertex) -> bool:
        return self._canonical(u, v)

    @staticmethod
    def _canonical(a: Vertex, b: Vertex) -> bool:
        # simple canonical order by string id
        return str(a.id) <= str(b.id)
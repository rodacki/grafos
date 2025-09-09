from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from .vertex import Vertex

@dataclass(frozen=True, slots=True)
class Edge:
    """Aresta imutável. Em grafos não dirigidos, (u,v) e (v,u) são tratados pela classe do grafo."""
    u: Vertex
    v: Vertex
    weight: float | None = None
    data: Any = None

    def __str__(self) -> str:
        w = f", w={self.weight}" if self.weight is not None else ""
        return f"Edge({self.u.id} -> {self.v.id}{w})"
    
    
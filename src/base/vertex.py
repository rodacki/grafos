from __future__ import annotations
from dataclasses import dataclass
from typing import Hashable, Any

@dataclass(frozen=True, slots=True)
class Vertex:
    """Vértice identificável e hashable. O 'id' deve ser estável (str/int)."""
    id: Hashable
    data: Any = None

    def __str__(self) -> str:
        return f"Vertex({self.id})"

    def __hash__(self) -> int:
        # hash apenas do identificador garante unicidade no grafo
        return hash(self.id)
from enum import Enum, auto

class Color(Enum):
    """Vertex colors used in BFS/DFS (CLRS style).
    
    - WHITE: undiscovered
    - GRAY: discovered but not fully explored
    - BLACK: fully explored
    """
    WHITE = auto()
    GRAY = auto()
    BLACK = auto()
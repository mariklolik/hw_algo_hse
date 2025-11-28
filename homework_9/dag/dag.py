from __future__ import annotations

from typing import Dict, List, Optional, Tuple, TypeVar

T = TypeVar("T")

WHITE = 0
GRAY = 1
BLACK = 2


def detect_cycle(graph: Dict[T, List[T]]) -> Tuple[bool, List[T]]:
    if not graph:
        return False, []
    
    color: Dict[T, int] = {v: WHITE for v in graph}
    parent: Dict[T, Optional[T]] = {v: None for v in graph}
    
    for vertex in graph:
        if color[vertex] == WHITE:
            has_cycle, cycle = _dfs_cycle(graph, vertex, color, parent)
            if has_cycle:
                return True, cycle
    
    return False, []


def _dfs_cycle(
    graph: Dict[T, List[T]],
    vertex: T,
    color: Dict[T, int],
    parent: Dict[T, Optional[T]]
) -> Tuple[bool, List[T]]:
    color[vertex] = GRAY
    
    for neighbor in graph.get(vertex, []):
        if neighbor not in color:
            color[neighbor] = WHITE
            parent[neighbor] = None
        
        if color[neighbor] == GRAY:
            cycle = _reconstruct_cycle(parent, vertex, neighbor)
            return True, cycle
        
        if color[neighbor] == WHITE:
            parent[neighbor] = vertex
            has_cycle, cycle = _dfs_cycle(graph, neighbor, color, parent)
            if has_cycle:
                return True, cycle
    
    color[vertex] = BLACK
    return False, []


def _reconstruct_cycle(
    parent: Dict[T, Optional[T]],
    end: T,
    start: T
) -> List[T]:
    cycle = [start]
    current: Optional[T] = end
    
    while current is not None and current != start:
        cycle.append(current)
        current = parent.get(current)
    
    cycle.append(start)
    cycle.reverse()
    return cycle


def topological_sort(graph: Dict[T, List[T]]) -> Optional[List[T]]:
    has_cycle, _ = detect_cycle(graph)
    if has_cycle:
        return None
    
    if not graph:
        return []
    
    visited: set = set()
    result: List[T] = []
    
    for vertex in graph:
        if vertex not in visited:
            _dfs_topsort(graph, vertex, visited, result)
    
    result.reverse()
    return result


def _dfs_topsort(
    graph: Dict[T, List[T]],
    vertex: T,
    visited: set,
    result: List[T]
) -> None:
    visited.add(vertex)
    
    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            _dfs_topsort(graph, neighbor, visited, result)
    
    result.append(vertex)


def process_dag(graph: Dict[T, List[T]]) -> Tuple[bool, List[T]]:
    has_cycle, cycle = detect_cycle(graph)
    
    if has_cycle:
        return True, cycle
    
    topsort = topological_sort(graph)
    return False, topsort if topsort is not None else []


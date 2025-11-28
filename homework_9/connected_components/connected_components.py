from __future__ import annotations

from typing import Dict, List, Set, TypeVar

T = TypeVar("T")


def find_connected_components(graph: Dict[T, List[T]]) -> List[Set[T]]:
    if not graph:
        return []
    
    visited: Set[T] = set()
    components: List[Set[T]] = []
    
    for vertex in graph:
        if vertex not in visited:
            component = _bfs(graph, vertex, visited)
            components.append(component)
    
    return components


def _bfs(graph: Dict[T, List[T]], start: T, visited: Set[T]) -> Set[T]:
    component: Set[T] = set()
    queue = [start]
    visited.add(start)
    
    while queue:
        vertex = queue.pop(0)
        component.add(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return component


def find_connected_components_dfs(graph: Dict[T, List[T]]) -> List[Set[T]]:
    if not graph:
        return []
    
    visited: Set[T] = set()
    components: List[Set[T]] = []
    
    for vertex in graph:
        if vertex not in visited:
            component: Set[T] = set()
            _dfs(graph, vertex, visited, component)
            components.append(component)
    
    return components


def _dfs(graph: Dict[T, List[T]], vertex: T, visited: Set[T], component: Set[T]) -> None:
    visited.add(vertex)
    component.add(vertex)
    
    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            _dfs(graph, neighbor, visited, component)


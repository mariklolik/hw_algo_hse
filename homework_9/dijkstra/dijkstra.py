from __future__ import annotations

import heapq
from typing import Dict, List, Optional, Tuple, TypeVar

T = TypeVar("T")

INF = float("inf")


def dijkstra(
    graph: Dict[T, List[Tuple[T, float]]],
    start: T
) -> Tuple[Dict[T, float], Dict[T, Optional[T]]]:
    if start not in graph:
        raise ValueError(f"Start vertex {start} not in graph")
    
    distances: Dict[T, float] = {v: INF for v in graph}
    distances[start] = 0
    
    previous: Dict[T, Optional[T]] = {v: None for v in graph}
    
    heap: List[Tuple[float, T]] = [(0, start)]
    visited: set = set()
    
    while heap:
        current_dist, current = heapq.heappop(heap)
        
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor, weight in graph.get(current, []):
            if weight < 0:
                raise ValueError("Dijkstra does not support negative weights")
            
            if neighbor not in distances:
                distances[neighbor] = INF
                previous[neighbor] = None
            
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current
                heapq.heappush(heap, (new_dist, neighbor))
    
    return distances, previous


def shortest_path(
    graph: Dict[T, List[Tuple[T, float]]],
    start: T,
    end: T
) -> Tuple[float, List[T]]:
    if start not in graph:
        raise ValueError(f"Start vertex {start} not in graph")
    
    distances, previous = dijkstra(graph, start)
    
    if end not in distances or distances[end] == INF:
        return INF, []
    
    path = []
    current: Optional[T] = end
    while current is not None:
        path.append(current)
        current = previous.get(current)
    
    path.reverse()
    return distances[end], path


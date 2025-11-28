import unittest

from homework_9.dijkstra.dijkstra import (
    INF,
    dijkstra,
    shortest_path,
)


class TestDijkstra(unittest.TestCase):
    def test_simple_graph(self):
        graph = {
            "A": [("B", 1), ("C", 4)],
            "B": [("A", 1), ("C", 2), ("D", 5)],
            "C": [("A", 4), ("B", 2), ("D", 1)],
            "D": [("B", 5), ("C", 1)]
        }
        distances, _ = dijkstra(graph, "A")
        
        self.assertEqual(distances["A"], 0)
        self.assertEqual(distances["B"], 1)
        self.assertEqual(distances["C"], 3)
        self.assertEqual(distances["D"], 4)
    
    def test_single_vertex(self):
        graph = {"A": []}
        distances, previous = dijkstra(graph, "A")
        
        self.assertEqual(distances["A"], 0)
        self.assertIsNone(previous["A"])
    
    def test_two_vertices(self):
        graph = {
            "A": [("B", 5)],
            "B": [("A", 5)]
        }
        distances, previous = dijkstra(graph, "A")
        
        self.assertEqual(distances["A"], 0)
        self.assertEqual(distances["B"], 5)
        self.assertEqual(previous["B"], "A")
    
    def test_disconnected_graph(self):
        graph = {
            "A": [("B", 1)],
            "B": [("A", 1)],
            "C": [],
            "D": [("C", 2)]
        }
        distances, _ = dijkstra(graph, "A")
        
        self.assertEqual(distances["A"], 0)
        self.assertEqual(distances["B"], 1)
        self.assertEqual(distances["C"], INF)
        self.assertEqual(distances["D"], INF)
    
    def test_directed_graph(self):
        graph = {
            "A": [("B", 1)],
            "B": [("C", 2)],
            "C": []
        }
        distances, _ = dijkstra(graph, "A")
        
        self.assertEqual(distances["A"], 0)
        self.assertEqual(distances["B"], 1)
        self.assertEqual(distances["C"], 3)
    
    def test_multiple_paths_same_distance(self):
        graph = {
            "A": [("B", 1), ("C", 1)],
            "B": [("D", 1)],
            "C": [("D", 1)],
            "D": []
        }
        distances, _ = dijkstra(graph, "A")
        
        self.assertEqual(distances["D"], 2)
    
    def test_zero_weight_edges(self):
        graph = {
            "A": [("B", 0)],
            "B": [("C", 0)],
            "C": []
        }
        distances, _ = dijkstra(graph, "A")
        
        self.assertEqual(distances["A"], 0)
        self.assertEqual(distances["B"], 0)
        self.assertEqual(distances["C"], 0)
    
    def test_float_weights(self):
        graph = {
            "A": [("B", 1.5)],
            "B": [("C", 2.5)],
            "C": []
        }
        distances, _ = dijkstra(graph, "A")
        
        self.assertAlmostEqual(distances["C"], 4.0)
    
    def test_integer_vertices(self):
        graph = {
            1: [(2, 10), (3, 5)],
            2: [(3, 2), (4, 1)],
            3: [(2, 3), (4, 9)],
            4: []
        }
        distances, _ = dijkstra(graph, 1)
        
        self.assertEqual(distances[1], 0)
        self.assertEqual(distances[2], 8)
        self.assertEqual(distances[3], 5)
        self.assertEqual(distances[4], 9)
    
    def test_start_not_in_graph(self):
        graph = {"A": [], "B": []}
        with self.assertRaises(ValueError):
            dijkstra(graph, "C")
    
    def test_negative_weight_raises(self):
        graph = {
            "A": [("B", -1)],
            "B": []
        }
        with self.assertRaises(ValueError):
            dijkstra(graph, "A")
    
    def test_self_loop(self):
        graph = {
            "A": [("A", 5), ("B", 1)],
            "B": []
        }
        distances, _ = dijkstra(graph, "A")
        
        self.assertEqual(distances["A"], 0)
        self.assertEqual(distances["B"], 1)
    
    def test_complex_graph(self):
        graph = {
            "S": [("A", 7), ("B", 2), ("C", 3)],
            "A": [("S", 7), ("B", 3), ("D", 4)],
            "B": [("S", 2), ("A", 3), ("D", 4), ("H", 1)],
            "C": [("S", 3), ("L", 2)],
            "D": [("A", 4), ("B", 4), ("F", 5)],
            "H": [("B", 1), ("F", 3), ("G", 2)],
            "L": [("C", 2), ("I", 4), ("J", 4)],
            "F": [("D", 5), ("H", 3)],
            "G": [("H", 2), ("E", 2)],
            "I": [("L", 4), ("J", 6), ("K", 4)],
            "J": [("L", 4), ("I", 6), ("K", 4)],
            "K": [("I", 4), ("J", 4), ("E", 5)],
            "E": [("G", 2), ("K", 5)]
        }
        distances, _ = dijkstra(graph, "S")
        
        self.assertEqual(distances["S"], 0)
        self.assertEqual(distances["B"], 2)
        self.assertEqual(distances["H"], 3)
        self.assertEqual(distances["G"], 5)
        self.assertEqual(distances["E"], 7)
    
    def test_neighbor_not_in_graph_keys(self):
        graph = {
            "A": [("B", 1), ("C", 2)],
            "B": []
        }
        distances, _ = dijkstra(graph, "A")
        
        self.assertEqual(distances["A"], 0)
        self.assertEqual(distances["B"], 1)
        self.assertEqual(distances["C"], 2)


class TestShortestPath(unittest.TestCase):
    def test_simple_path(self):
        graph = {
            "A": [("B", 1), ("C", 4)],
            "B": [("C", 2)],
            "C": []
        }
        distance, path = shortest_path(graph, "A", "C")
        
        self.assertEqual(distance, 3)
        self.assertEqual(path, ["A", "B", "C"])
    
    def test_direct_path(self):
        graph = {
            "A": [("B", 5)],
            "B": []
        }
        distance, path = shortest_path(graph, "A", "B")
        
        self.assertEqual(distance, 5)
        self.assertEqual(path, ["A", "B"])
    
    def test_same_start_end(self):
        graph = {"A": [("B", 1)], "B": []}
        distance, path = shortest_path(graph, "A", "A")
        
        self.assertEqual(distance, 0)
        self.assertEqual(path, ["A"])
    
    def test_no_path_exists(self):
        graph = {
            "A": [],
            "B": []
        }
        distance, path = shortest_path(graph, "A", "B")
        
        self.assertEqual(distance, INF)
        self.assertEqual(path, [])
    
    def test_end_not_in_graph(self):
        graph = {"A": [], "B": []}
        distance, path = shortest_path(graph, "A", "C")
        
        self.assertEqual(distance, INF)
        self.assertEqual(path, [])
    
    def test_longer_path(self):
        graph = {
            1: [(2, 1)],
            2: [(3, 1)],
            3: [(4, 1)],
            4: [(5, 1)],
            5: []
        }
        distance, path = shortest_path(graph, 1, 5)
        
        self.assertEqual(distance, 4)
        self.assertEqual(path, [1, 2, 3, 4, 5])
    
    def test_chooses_shorter_path(self):
        graph = {
            "A": [("B", 1), ("C", 10)],
            "B": [("C", 1)],
            "C": []
        }
        distance, path = shortest_path(graph, "A", "C")
        
        self.assertEqual(distance, 2)
        self.assertEqual(path, ["A", "B", "C"])
    
    def test_start_not_in_graph(self):
        graph = {"A": [], "B": []}
        with self.assertRaises(ValueError):
            shortest_path(graph, "X", "A")


class TestEdgeCases(unittest.TestCase):
    def test_empty_adjacency_lists(self):
        graph = {"A": [], "B": [], "C": []}
        distances, _ = dijkstra(graph, "A")
        
        self.assertEqual(distances["A"], 0)
        self.assertEqual(distances["B"], INF)
        self.assertEqual(distances["C"], INF)
    
    def test_large_weights(self):
        graph = {
            "A": [("B", 1e10)],
            "B": [("C", 1e10)],
            "C": []
        }
        distances, _ = dijkstra(graph, "A")
        
        self.assertEqual(distances["C"], 2e10)
    
    def test_many_edges_from_single_vertex(self):
        graph = {"A": [(chr(ord("B") + i), i + 1) for i in range(10)]}
        for i in range(10):
            graph[chr(ord("B") + i)] = []
        
        distances, _ = dijkstra(graph, "A")
        
        self.assertEqual(distances["A"], 0)
        for i in range(10):
            self.assertEqual(distances[chr(ord("B") + i)], i + 1)
    
    def test_cycle_in_graph(self):
        graph = {
            "A": [("B", 1)],
            "B": [("C", 1)],
            "C": [("A", 1)]
        }
        distances, _ = dijkstra(graph, "A")
        
        self.assertEqual(distances["A"], 0)
        self.assertEqual(distances["B"], 1)
        self.assertEqual(distances["C"], 2)


if __name__ == "__main__":
    unittest.main()


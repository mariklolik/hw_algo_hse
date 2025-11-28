import unittest

from homework_9.dag.dag import (
    detect_cycle,
    process_dag,
    topological_sort,
)


class TestDetectCycle(unittest.TestCase):
    def test_empty_graph(self):
        graph = {}
        has_cycle, cycle = detect_cycle(graph)
        self.assertFalse(has_cycle)
        self.assertEqual(cycle, [])
    
    def test_single_vertex_no_cycle(self):
        graph = {1: []}
        has_cycle, cycle = detect_cycle(graph)
        self.assertFalse(has_cycle)
        self.assertEqual(cycle, [])
    
    def test_single_vertex_self_loop(self):
        graph = {1: [1]}
        has_cycle, cycle = detect_cycle(graph)
        self.assertTrue(has_cycle)
        self.assertEqual(len(cycle), 2)
        self.assertEqual(cycle[0], cycle[-1])
    
    def test_two_vertices_no_cycle(self):
        graph = {1: [2], 2: []}
        has_cycle, cycle = detect_cycle(graph)
        self.assertFalse(has_cycle)
        self.assertEqual(cycle, [])
    
    def test_two_vertices_cycle(self):
        graph = {1: [2], 2: [1]}
        has_cycle, cycle = detect_cycle(graph)
        self.assertTrue(has_cycle)
        self.assertGreater(len(cycle), 1)
        self.assertEqual(cycle[0], cycle[-1])
    
    def test_three_vertices_cycle(self):
        graph = {1: [2], 2: [3], 3: [1]}
        has_cycle, cycle = detect_cycle(graph)
        self.assertTrue(has_cycle)
        self.assertEqual(cycle[0], cycle[-1])
        self.assertGreaterEqual(len(cycle), 3)
    
    def test_dag_no_cycle(self):
        graph = {
            1: [2, 3],
            2: [4],
            3: [4],
            4: []
        }
        has_cycle, cycle = detect_cycle(graph)
        self.assertFalse(has_cycle)
        self.assertEqual(cycle, [])
    
    def test_disconnected_with_cycle(self):
        graph = {
            1: [2],
            2: [],
            3: [4],
            4: [5],
            5: [3]
        }
        has_cycle, cycle = detect_cycle(graph)
        self.assertTrue(has_cycle)
        self.assertEqual(cycle[0], cycle[-1])
    
    def test_disconnected_no_cycle(self):
        graph = {
            1: [2],
            2: [],
            3: [4],
            4: []
        }
        has_cycle, cycle = detect_cycle(graph)
        self.assertFalse(has_cycle)
    
    def test_complex_graph_with_cycle(self):
        graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["D", "E"],
            "D": ["F"],
            "E": ["F"],
            "F": ["C"]
        }
        has_cycle, cycle = detect_cycle(graph)
        self.assertTrue(has_cycle)
        self.assertEqual(cycle[0], cycle[-1])
    
    def test_complex_dag(self):
        graph = {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "C": ["E", "F"],
            "D": ["G"],
            "E": ["G", "H"],
            "F": ["H"],
            "G": [],
            "H": []
        }
        has_cycle, cycle = detect_cycle(graph)
        self.assertFalse(has_cycle)
    
    def test_long_chain_no_cycle(self):
        n = 100
        graph = {i: [i + 1] for i in range(n)}
        graph[n] = []
        has_cycle, cycle = detect_cycle(graph)
        self.assertFalse(has_cycle)
    
    def test_long_chain_with_back_edge(self):
        n = 10
        graph = {i: [i + 1] for i in range(n)}
        graph[n] = [0]
        has_cycle, cycle = detect_cycle(graph)
        self.assertTrue(has_cycle)
    
    def test_multiple_cycles(self):
        graph = {
            1: [2],
            2: [1, 3],
            3: [4],
            4: [3]
        }
        has_cycle, cycle = detect_cycle(graph)
        self.assertTrue(has_cycle)
        self.assertEqual(cycle[0], cycle[-1])
    
    def test_neighbor_not_in_keys(self):
        graph = {1: [2, 3], 2: []}
        has_cycle, cycle = detect_cycle(graph)
        self.assertFalse(has_cycle)


class TestTopologicalSort(unittest.TestCase):
    def test_empty_graph(self):
        graph = {}
        result = topological_sort(graph)
        self.assertEqual(result, [])
    
    def test_single_vertex(self):
        graph = {1: []}
        result = topological_sort(graph)
        self.assertEqual(result, [1])
    
    def test_two_vertices(self):
        graph = {1: [2], 2: []}
        result = topological_sort(graph)
        self.assertIsNotNone(result)
        self.assertEqual(result.index(1), 0)
        self.assertEqual(result.index(2), 1)
    
    def test_simple_dag(self):
        graph = {
            1: [2, 3],
            2: [4],
            3: [4],
            4: []
        }
        result = topological_sort(graph)
        self.assertIsNotNone(result)
        self.assertLess(result.index(1), result.index(2))
        self.assertLess(result.index(1), result.index(3))
        self.assertLess(result.index(2), result.index(4))
        self.assertLess(result.index(3), result.index(4))
    
    def test_graph_with_cycle_returns_none(self):
        graph = {1: [2], 2: [3], 3: [1]}
        result = topological_sort(graph)
        self.assertIsNone(result)
    
    def test_disconnected_dag(self):
        graph = {
            1: [2],
            2: [],
            3: [4],
            4: []
        }
        result = topological_sort(graph)
        self.assertIsNotNone(result)
        self.assertLess(result.index(1), result.index(2))
        self.assertLess(result.index(3), result.index(4))
    
    def test_diamond_dag(self):
        graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["D"],
            "D": []
        }
        result = topological_sort(graph)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], "A")
        self.assertEqual(result[-1], "D")
    
    def test_linear_graph(self):
        graph = {1: [2], 2: [3], 3: [4], 4: [5], 5: []}
        result = topological_sort(graph)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_multiple_valid_orderings(self):
        graph = {
            1: [],
            2: [],
            3: [1, 2]
        }
        result = topological_sort(graph)
        self.assertIsNotNone(result)
        self.assertLess(result.index(3), result.index(1))
        self.assertLess(result.index(3), result.index(2))
    
    def test_all_isolated_vertices(self):
        graph = {1: [], 2: [], 3: [], 4: []}
        result = topological_sort(graph)
        self.assertIsNotNone(result)
        self.assertEqual(set(result), {1, 2, 3, 4})
    
    def test_complex_dag(self):
        graph = {
            "shirt": [],
            "tie": ["shirt"],
            "jacket": ["shirt", "tie"],
            "belt": [],
            "pants": ["belt"],
            "shoes": ["pants"]
        }
        result = topological_sort(graph)
        self.assertIsNotNone(result)
        
        self.assertLess(result.index("tie"), result.index("shirt"))
        self.assertLess(result.index("jacket"), result.index("shirt"))
        self.assertLess(result.index("jacket"), result.index("tie"))
        self.assertLess(result.index("pants"), result.index("belt"))
        self.assertLess(result.index("shoes"), result.index("pants"))


class TestProcessDag(unittest.TestCase):
    def test_empty_graph(self):
        graph = {}
        has_cycle, result = process_dag(graph)
        self.assertFalse(has_cycle)
        self.assertEqual(result, [])
    
    def test_dag_returns_topsort(self):
        graph = {1: [2], 2: [3], 3: []}
        has_cycle, result = process_dag(graph)
        self.assertFalse(has_cycle)
        self.assertEqual(result, [1, 2, 3])
    
    def test_cycle_returns_cycle(self):
        graph = {1: [2], 2: [3], 3: [1]}
        has_cycle, result = process_dag(graph)
        self.assertTrue(has_cycle)
        self.assertEqual(result[0], result[-1])
        self.assertGreater(len(result), 1)
    
    def test_self_loop_returns_cycle(self):
        graph = {1: [1]}
        has_cycle, result = process_dag(graph)
        self.assertTrue(has_cycle)
        self.assertEqual(result[0], result[-1])
    
    def test_complex_dag(self):
        graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["D"],
            "D": []
        }
        has_cycle, result = process_dag(graph)
        self.assertFalse(has_cycle)
        self.assertEqual(result[0], "A")
        self.assertEqual(result[-1], "D")
    
    def test_complex_cycle(self):
        graph = {
            "A": ["B"],
            "B": ["C"],
            "C": ["D"],
            "D": ["B"]
        }
        has_cycle, result = process_dag(graph)
        self.assertTrue(has_cycle)
        self.assertIn("B", result)
        self.assertIn("C", result)
        self.assertIn("D", result)


class TestEdgeCases(unittest.TestCase):
    def test_cycle_validation(self):
        graph = {1: [2], 2: [3], 3: [1]}
        has_cycle, cycle = detect_cycle(graph)
        self.assertTrue(has_cycle)
        
        for i in range(len(cycle) - 1):
            current = cycle[i]
            next_vertex = cycle[i + 1]
            self.assertIn(next_vertex, graph.get(current, []))
    
    def test_topsort_validation(self):
        graph = {
            1: [2, 3],
            2: [4],
            3: [4],
            4: []
        }
        result = topological_sort(graph)
        self.assertIsNotNone(result)
        
        position = {v: i for i, v in enumerate(result)}
        for vertex, neighbors in graph.items():
            for neighbor in neighbors:
                self.assertLess(position[vertex], position[neighbor])
    
    def test_string_vertices(self):
        graph = {"a": ["b"], "b": ["c"], "c": []}
        has_cycle, _ = detect_cycle(graph)
        self.assertFalse(has_cycle)
        
        result = topological_sort(graph)
        self.assertEqual(result, ["a", "b", "c"])
    
    def test_mixed_vertex_types_not_recommended(self):
        graph = {1: [2], 2: []}
        has_cycle, _ = detect_cycle(graph)
        self.assertFalse(has_cycle)


if __name__ == "__main__":
    unittest.main()


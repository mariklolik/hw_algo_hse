import unittest

from homework_9.connected_components.connected_components import (
    find_connected_components,
    find_connected_components_dfs,
)


class TestConnectedComponentsBFS(unittest.TestCase):
    def test_empty_graph(self):
        graph = {}
        result = find_connected_components(graph)
        self.assertEqual(result, [])
    
    def test_single_vertex_no_edges(self):
        graph = {1: []}
        result = find_connected_components(graph)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {1})
    
    def test_single_vertex_self_loop(self):
        graph = {1: [1]}
        result = find_connected_components(graph)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {1})
    
    def test_two_vertices_connected(self):
        graph = {1: [2], 2: [1]}
        result = find_connected_components(graph)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {1, 2})
    
    def test_two_vertices_disconnected(self):
        graph = {1: [], 2: []}
        result = find_connected_components(graph)
        self.assertEqual(len(result), 2)
        components_as_sets = [comp for comp in result]
        self.assertIn({1}, components_as_sets)
        self.assertIn({2}, components_as_sets)
    
    def test_three_components(self):
        graph = {
            1: [2], 2: [1],
            3: [4, 5], 4: [3, 5], 5: [3, 4],
            6: []
        }
        result = find_connected_components(graph)
        self.assertEqual(len(result), 3)
        
        components_sorted = sorted(result, key=len)
        self.assertEqual(components_sorted[0], {6})
        self.assertEqual(components_sorted[1], {1, 2})
        self.assertEqual(components_sorted[2], {3, 4, 5})
    
    def test_fully_connected(self):
        graph = {
            1: [2, 3, 4],
            2: [1, 3, 4],
            3: [1, 2, 4],
            4: [1, 2, 3]
        }
        result = find_connected_components(graph)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {1, 2, 3, 4})
    
    def test_chain_graph(self):
        graph = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}
        result = find_connected_components(graph)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {1, 2, 3, 4})
    
    def test_star_graph(self):
        graph = {
            1: [2, 3, 4, 5],
            2: [1], 3: [1], 4: [1], 5: [1]
        }
        result = find_connected_components(graph)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {1, 2, 3, 4, 5})
    
    def test_cycle_graph(self):
        graph = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [3, 1]}
        result = find_connected_components(graph)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {1, 2, 3, 4})
    
    def test_string_vertices(self):
        graph = {"a": ["b"], "b": ["a"], "c": []}
        result = find_connected_components(graph)
        self.assertEqual(len(result), 2)
        
        components_sorted = sorted(result, key=len)
        self.assertEqual(components_sorted[0], {"c"})
        self.assertEqual(components_sorted[1], {"a", "b"})
    
    def test_multiple_isolated_vertices(self):
        graph = {1: [], 2: [], 3: [], 4: [], 5: []}
        result = find_connected_components(graph)
        self.assertEqual(len(result), 5)
        for comp in result:
            self.assertEqual(len(comp), 1)
    
    def test_two_equal_components(self):
        graph = {
            1: [2], 2: [1],
            3: [4], 4: [3]
        }
        result = find_connected_components(graph)
        self.assertEqual(len(result), 2)
        self.assertIn({1, 2}, result)
        self.assertIn({3, 4}, result)
    
    def test_asymmetric_adjacency_list(self):
        graph = {1: [2], 2: [], 3: []}
        result = find_connected_components(graph)
        self.assertEqual(len(result), 2)
        self.assertIn({1, 2}, result)
        self.assertIn({3}, result)
    
    def test_large_component(self):
        n = 100
        graph = {i: [i-1, i+1] for i in range(1, n)}
        graph[0] = [1]
        graph[n] = [n-1]
        result = find_connected_components(graph)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], set(range(n + 1)))
    
    def test_vertex_not_in_keys_but_in_neighbors(self):
        graph = {1: [2, 3], 2: [1]}
        result = find_connected_components(graph)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {1, 2, 3})


class TestConnectedComponentsDFS(unittest.TestCase):
    def test_empty_graph(self):
        graph = {}
        result = find_connected_components_dfs(graph)
        self.assertEqual(result, [])
    
    def test_single_vertex_no_edges(self):
        graph = {1: []}
        result = find_connected_components_dfs(graph)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {1})
    
    def test_single_vertex_self_loop(self):
        graph = {1: [1]}
        result = find_connected_components_dfs(graph)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {1})
    
    def test_two_vertices_connected(self):
        graph = {1: [2], 2: [1]}
        result = find_connected_components_dfs(graph)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {1, 2})
    
    def test_two_vertices_disconnected(self):
        graph = {1: [], 2: []}
        result = find_connected_components_dfs(graph)
        self.assertEqual(len(result), 2)
        components_as_sets = [comp for comp in result]
        self.assertIn({1}, components_as_sets)
        self.assertIn({2}, components_as_sets)
    
    def test_three_components(self):
        graph = {
            1: [2], 2: [1],
            3: [4, 5], 4: [3, 5], 5: [3, 4],
            6: []
        }
        result = find_connected_components_dfs(graph)
        self.assertEqual(len(result), 3)
        
        components_sorted = sorted(result, key=len)
        self.assertEqual(components_sorted[0], {6})
        self.assertEqual(components_sorted[1], {1, 2})
        self.assertEqual(components_sorted[2], {3, 4, 5})
    
    def test_fully_connected(self):
        graph = {
            1: [2, 3, 4],
            2: [1, 3, 4],
            3: [1, 2, 4],
            4: [1, 2, 3]
        }
        result = find_connected_components_dfs(graph)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {1, 2, 3, 4})
    
    def test_string_vertices(self):
        graph = {"a": ["b"], "b": ["a"], "c": []}
        result = find_connected_components_dfs(graph)
        self.assertEqual(len(result), 2)
        
        components_sorted = sorted(result, key=len)
        self.assertEqual(components_sorted[0], {"c"})
        self.assertEqual(components_sorted[1], {"a", "b"})


class TestBothMethodsEquivalence(unittest.TestCase):
    def test_same_result_simple(self):
        graph = {1: [2], 2: [1], 3: []}
        result_bfs = find_connected_components(graph)
        result_dfs = find_connected_components_dfs(graph)
        
        self.assertEqual(len(result_bfs), len(result_dfs))
        for comp in result_bfs:
            self.assertIn(comp, result_dfs)
    
    def test_same_result_complex(self):
        graph = {
            1: [2, 3], 2: [1], 3: [1],
            4: [5, 6, 7], 5: [4], 6: [4], 7: [4],
            8: [], 9: [], 10: []
        }
        result_bfs = find_connected_components(graph)
        result_dfs = find_connected_components_dfs(graph)
        
        self.assertEqual(len(result_bfs), len(result_dfs))
        for comp in result_bfs:
            self.assertIn(comp, result_dfs)
    
    def test_same_component_count(self):
        graph = {i: [] for i in range(10)}
        result_bfs = find_connected_components(graph)
        result_dfs = find_connected_components_dfs(graph)
        self.assertEqual(len(result_bfs), len(result_dfs))


if __name__ == "__main__":
    unittest.main()


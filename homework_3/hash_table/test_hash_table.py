import unittest
from .hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable()

    def test_insert_and_search(self):
        self.ht.insert("key1", "value1")
        self.assertEqual(self.ht.search("key1"), "value1")
        self.assertIsNone(self.ht.search("key2"))

    def test_delete(self):
        self.ht.insert("key1", "value1")
        self.ht.delete("key1")
        self.assertIsNone(self.ht.search("key1"))

    def test_update(self):
        self.ht.insert("key1", "value1")
        self.ht.insert("key1", "new_value")
        self.assertEqual(self.ht.search("key1"), "new_value")

    def test_collision(self):
        # These keys will likely collide with a small table size
        ht = HashTable(size=2)
        # Force collision by manipulating internal state for a predictable test
        # Note: This is generally not good practice but useful here for a deterministic test.
        # We find two keys that hash to the same bucket.
        key1 = "a"
        index1 = ht._hash(key1)

        key2 = "c"
        while ht._hash(key2) != index1:
            key2 += "c"

        ht.insert(key1, "value_a")
        ht.insert(key2, "value_c")
        
        self.assertEqual(ht.search(key1), "value_a")
        self.assertEqual(ht.search(key2), "value_c")
        self.assertEqual(len(ht.table[index1]), 2)
        
    def test_resize(self):
        self.ht = HashTable(size=2)
        self.ht.insert("key1", "value1")
        self.ht.insert("key2", "value2")
        self.assertEqual(self.ht.size, 2)
        self.ht.insert("key3", "value3")
        self.assertGreater(self.ht.size, 2)
        self.assertEqual(self.ht.search("key1"), "value1")
        self.assertEqual(self.ht.search("key2"), "value2")
        self.assertEqual(self.ht.search("key3"), "value3")

if __name__ == '__main__':
    unittest.main()

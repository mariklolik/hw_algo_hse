import unittest
from merge_lists import ListNode, merge_two_lists_dummy, merge_two_lists_no_dummy

def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

class TestMergeTwoLists(unittest.TestCase):

    def test_example_dummy(self):
        list1 = create_list([1, 2, 4])
        list2 = create_list([1, 3, 4])
        result = merge_two_lists_dummy(list1, list2)
        self.assertEqual(list_to_array(result), [1, 1, 2, 3, 4, 4])

    def test_example_no_dummy(self):
        list1 = create_list([1, 2, 4])
        list2 = create_list([1, 3, 4])
        result = merge_two_lists_no_dummy(list1, list2)
        self.assertEqual(list_to_array(result), [1, 1, 2, 3, 4, 4])

    def test_both_empty_dummy(self):
        result = merge_two_lists_dummy(None, None)
        self.assertIsNone(result)

    def test_both_empty_no_dummy(self):
        result = merge_two_lists_no_dummy(None, None)
        self.assertIsNone(result)

    def test_first_empty_dummy(self):
        list2 = create_list([1, 3, 4])
        result = merge_two_lists_dummy(None, list2)
        self.assertEqual(list_to_array(result), [1, 3, 4])

    def test_first_empty_no_dummy(self):
        list2 = create_list([1, 3, 4])
        result = merge_two_lists_no_dummy(None, list2)
        self.assertEqual(list_to_array(result), [1, 3, 4])

    def test_second_empty_dummy(self):
        list1 = create_list([1, 2, 4])
        result = merge_two_lists_dummy(list1, None)
        self.assertEqual(list_to_array(result), [1, 2, 4])

    def test_second_empty_no_dummy(self):
        list1 = create_list([1, 2, 4])
        result = merge_two_lists_no_dummy(list1, None)
        self.assertEqual(list_to_array(result), [1, 2, 4])

    def test_single_element_dummy(self):
        list1 = create_list([1])
        list2 = create_list([2])
        result = merge_two_lists_dummy(list1, list2)
        self.assertEqual(list_to_array(result), [1, 2])

    def test_single_element_no_dummy(self):
        list1 = create_list([1])
        list2 = create_list([2])
        result = merge_two_lists_no_dummy(list1, list2)
        self.assertEqual(list_to_array(result), [1, 2])

    def test_duplicates_dummy(self):
        list1 = create_list([1, 1, 3])
        list2 = create_list([1, 2, 2])
        result = merge_two_lists_dummy(list1, list2)
        self.assertEqual(list_to_array(result), [1, 1, 1, 2, 2, 3])

    def test_duplicates_no_dummy(self):
        list1 = create_list([1, 1, 3])
        list2 = create_list([1, 2, 2])
        result = merge_two_lists_no_dummy(list1, list2)
        self.assertEqual(list_to_array(result), [1, 1, 1, 2, 2, 3])

    def test_different_lengths_dummy(self):
        list1 = create_list([1, 3, 5, 7])
        list2 = create_list([2, 4])
        result = merge_two_lists_dummy(list1, list2)
        self.assertEqual(list_to_array(result), [1, 2, 3, 4, 5, 7])

    def test_different_lengths_no_dummy(self):
        list1 = create_list([1, 3, 5, 7])
        list2 = create_list([2, 4])
        result = merge_two_lists_no_dummy(list1, list2)
        self.assertEqual(list_to_array(result), [1, 2, 3, 4, 5, 7])

if __name__ == '__main__':
    unittest.main()

import unittest
import bubble_sort


class Tester(unittest.TestCase):
    def setUp(self):
        self.bsfn = bubble_sort
        self.test_list = [2,3,-4,9,7]
        self.bubble_sort_result = [-4,2,3,7,9]

    def test_bubble_sort(self):
        """testing bubble sort"""
        self.assertEqual(
            self.bsfn.bubble_sort(self.test_list),
            self.bubble_sort_result
        )

if __name__ == "__main__":
    unittest.main()
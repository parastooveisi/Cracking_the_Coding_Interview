import unittest
from tree_traversal import *

root = Node(27)
root.left = Node(14)
root.right = Node(35)
root.left.left = Node(10)
root.left.right = Node(19)
root.right.left = Node(31)
root.right.right = Node(42)


class test_traversals(unittest.TestCase):

    def test_in_order(self):
        result = in_order_traversal(root)
        self.assertEqual(result, [10, 14, 19, 27, 31, 35, 42])

    def test_pre_order(self):
        result = pre_order_traversal(root)
        self.assertEqual(result, [27, 14, 10, 19, 35, 31, 42])

    def test_post_order(self):
        result = post_order_traversal(root)
        self.assertEqual(result, [10, 19, 14, 31, 42, 35, 27])


if __name__ == '__main__':
    unittest.main()

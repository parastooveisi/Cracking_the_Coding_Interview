import unittest
from binary_search_tree import BinarySearchTree


class test_BST(unittest.TestCase):

    def test_insert(self):
        BST = BinarySearchTree()
        BST.insert(10)
        BST.insert(6)
        BST.insert(13)
        BST.insert(8)
        BST.insert(12)
        self.assertEqual(BST.root.data, 10)
        self.assertEqual(BST.root.left.data, 6)
        self.assertEqual(BST.root.right.data, 13)
        self.assertEqual(BST.root.left.right.data, 8)
        self.assertEqual(BST.root.right.left.data, 12)

    def test_lookup(self):
        BST = BinarySearchTree()
        self.assertEqual(BST.lookup(10), False)  # Empty tree
        BST.insert(10)
        BST.insert(6)
        BST.insert(13)
        BST.insert(8)
        BST.insert(12)
        self.assertEqual(BST.lookup(13), True)
        self.assertEqual(BST.lookup(20), False)


if __name__ == '__main__':
    unittest.main()

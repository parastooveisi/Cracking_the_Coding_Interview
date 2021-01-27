from linked_list import LinkedList
from binary_search_tree import BinarySearchTree


def lists_of_depth(root):
    result = {}
    queue = []
    queue.append((root, 0))
    while queue:
        node, level = queue.pop(0)
        if level not in result:
            result[level] = LinkedList()

        result[level].append(node.data)

        if node.left:
            queue.append((node.left, level + 1))

        if node.right:
            queue.append((node.right, level + 1))

    return result


def example():
    BST = BinarySearchTree()
    BST.insert(10)
    BST.insert(6)
    BST.insert(13)
    BST.insert(8)
    BST.insert(12)
    result = lists_of_depth(BST.root)
    for llist in result.values():
        llist.print_list()


if __name__ == "__main__":
    example()

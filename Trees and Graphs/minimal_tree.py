from tree_traversal import Node


def convert_to_tree(inputarr):
    if not inputarr:
        return None

    mid = len(inputarr) // 2
    root = Node(inputarr[mid])
    print(root.data)
    root.left = convert_to_tree(inputarr[:mid])
    root.right = convert_to_tree(inputarr[mid+1:])
    return root


convert_to_tree([1, 2, 3, 4, 5, 6, 7])

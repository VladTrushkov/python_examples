# Первый вывод дерева, в принципе, не нужен
def print_tree_ver_1(node):
    print(node.operation)
    if not isinstance(node.left, Node) and not isinstance(node.right, Node):
        print(node.left, node.right)
        return
    if not isinstance(node.left, Node):
        print(node.left)
        print_tree(node.right)
        return
    if not isinstance(node.right, Node):
        print(node.right)
        print_tree(node.left)
        return
    print_tree(node.left)
    print_tree(node.right)
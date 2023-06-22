count_space = 0


def print_tree(node, one_space=4):
    global count_space
    if not isinstance(node, Node):
        print(f"{count_space * ' '}{node}")
        if count_space != 0:
            count_space -= one_space
        return
    count_space += one_space
    print_tree(node.left)
    print(f"{count_space * ' '}{node.operation}")
    count_space += one_space
    print_tree(node.right)
    count_space -= one_space


# Первый вывод дерева, в принципе не нужен
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


class Node:
    def __init__(self, operation, left, right):
        self.operation = operation
        self.left = left
        self.right = right


# string = "5 + 6 * 7 + 8 * 4"
string = "a * b * c + a + a * b"
# string = "2 * 3 + 4 * 5"
data = string.split()

stack = []
i = 0

while i < len(data):
    if not isinstance(data[i], Node) and data[i] in "*/":
        operation = data[i]
        left = stack.pop()
        right = data[i + 1]
        node = Node(operation, left, right)
        stack.append(node)
        i += 1
    else:
        stack.append(data[i])
    i += 1

data = stack.copy()
stack = []
i = 0
while i < len(data):
    if not isinstance(data[i], Node) and data[i] in "+-":
        operation = data[i]
        left = stack.pop()
        right = data[i + 1]
        node = Node(operation, left, right)
        stack.append(node)
        i += 1
    else:
        stack.append(data[i])
    i += 1


root = stack[0]
print_tree(root)

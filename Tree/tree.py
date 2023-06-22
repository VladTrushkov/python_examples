count_space = 0


class Node:
    def __init__(self, operation, left, right):
        self.operation = operation
        self.left = left
        self.right = right


def create_tree(data):
    stack = []
    list_of_operations = ["^", "*/", "+-"]  # список операций сгрупированных по приотритетам
    for operations in list_of_operations:
        i = 0
        while i < len(data):
            if not isinstance(data[i], Node) and data[i] in operations:
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
        stack.clear()
    return data[0]


def print_tree(node, indent=4):
    global count_space
    if not isinstance(node, Node):
        print(f"{count_space * ' '}{node}")
        if count_space != 0:
            count_space -= indent
        return
    count_space += indent
    print_tree(node.left)
    print(f"{count_space * ' '}{node.operation}")
    count_space += indent
    print_tree(node.right)
    count_space -= indent


# string = "5 + 6 * 7 + 8 * 4"
# string = "a * b * c + a + a * b"
# string = "2 * 3 + 4 * 5"
string = "1 * 2 + 2 * 3 + 4 * 5 + 6 * 7"
data = string.split()
tree_root = create_tree(data)
print_tree(tree_root)

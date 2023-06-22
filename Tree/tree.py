count_space = 0


class Node:
    def __init__(self, value, left, right, leaf=False):
        self.value = value
        self.left = left
        self.right = right
        self.leaf = leaf

    def set_leaf(self):
        self.leaf = True

    def it_is_leaf(self):
        return self.leaf


def create_tree(data):
    # Создание узлов листьев
    all_operations = "+-*/^"
    for i in range(len(data)):
        if data[i] not in all_operations:
            data[i] = Node(data[i], None, None, leaf=True)

    # Создание узлов операций
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


def simplify_tree(node):
    if node.left.it_is_leaf() and node.right.it_is_leaf():
        operation = node.value
        operand_1 = float(node.left.value)
        operand_2 = float(node.right.value)
        if operation == '+':
            result = operand_1 + operand_2
        elif operation == '-':
            result = operand_1 - operand_2
        elif operation == '*':
            result = operand_1 * operand_2
        elif operation == '/':
            result = operand_1 / operand_2
        elif operation == '^':
            result = operand_1 ** operand_2
        else:
            result = "operation not found"
        return Node(str(result), None, None, leaf=True)
    node.left = simplify_tree(node.left)
    node.right = simplify_tree(node.right)
    return simplify_tree(node)


def print_tree(node, indent=4):
    global count_space
    if not isinstance(node, Node):
        if node is not None:
            print(f"{count_space * ' '}{node.value}")
        if count_space >= indent:
            count_space -= indent
        return
    count_space += indent
    print_tree(node.left)
    print(f"{count_space * ' '}{node.value}")
    count_space += indent
    print_tree(node.right)
    if count_space >= indent:
        count_space -= indent


# TESTS
# Валидность данных должна быть обеспечена. Строка не пустая.
# string = "5 + 6 * 7 + 8 * 4"
# string = "a * b * c + a + a * b"
# string = "2 * 3 + 4 * 5"
# string = "1 * 2 + 2 * 3 + 4 * 5 + 6 * 7"
# string = "a"
# string = "1 + 2"
data = string.split()
tree = create_tree(data)
print_tree(tree)
tree = simplify_tree(tree)
print_tree(tree)
count_space = 0


def is_number(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


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


# def simplify_tree(node):
#     # Пока не работает, когда есть буквы
#     if node.left is None and node.right is None:
#         return node
#     if node.left.it_is_leaf() and node.right.it_is_leaf():
#         operation = node.value
#         operand_1 = node.left.value
#         operand_2 = node.right.value
#         if is_number(operand_1) and is_number(operand_2):
#             operand_1 = float(operand_1)
#             operand_2 = float(operand_2)
#             if operation == '+':
#                 result = operand_1 + operand_2
#             elif operation == '-':
#                 result = operand_1 - operand_2
#             elif operation == '*':
#                 result = operand_1 * operand_2
#             elif operation == '/':
#                 result = operand_1 / operand_2
#             elif operation == '^':
#                 result = operand_1 ** operand_2
#             else:
#                 result = "operation not found"
#             return Node(str(result), None, None, leaf=True)
#         return node

#     node.left = simplify_tree(node.left)
#     node.right = simplify_tree(node.right)
#     # if not node.left.it_is_leaf() and not node.right.it_is_leaf():
#     #     return node
#     return simplify_tree(node)


def find_multipliers(node, multipliers_list):
    # Если между всеми элементами операция умножение, то собираем все листья
    # 2 * 3 * a * b * c * d * e
    if node.it_is_leaf():
        multipliers_list.append(node.value)
        return
    find_multipliers(node.left, multipliers_list)
    find_multipliers(node.right, multipliers_list)


def intersection_list(list_1, list_2):
    for i in range(len(list_1) - 1, -1, -1):
        if list_1[i] not in list_2:
            list_1.pop(i)


def find_take_out_multiplier(node, multipliers_list, first_start=True):
    multipliers_list_2 = []
    if first_start:
        find_multipliers(node.right, multipliers_list)
    else:
        find_multipliers(node.right, multipliers_list_2)
        intersection_list(multipliers_list, multipliers_list_2)
    print(multipliers_list)

    multipliers_list_2 = []
    if node.left.value == "*":
        find_multipliers(node.left, multipliers_list_2)
        intersection_list(multipliers_list, multipliers_list_2)
    else:
        find_take_out_multiplier(node.left, multipliers_list, first_start=False)


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
# string = "1 + 2.0"
# string = "2 ^ 2 + 3 * 4 * 5 + 2 * 4 - 3 * 2 ^ 4"  # 24
# string = "1 + a"
# string = "a + b + c"
# string = "1 + 2 * a + 3 * b  + 4 * c + 5 * a * b + 6 * a * c + 7 * a * b * c"
# string = "a + a * b + a * c"
# string = "a * b * c * d * e"
string = "a * b * c + a * b + a"
data = string.split()
tree = create_tree(data)
print_tree(tree)
multipliers_list = []
find_take_out_multiplier(tree, multipliers_list)
print(multipliers_list)
# tree = simplify_tree(tree)
# print_tree(tree)
from collections import defaultdict

N = int(input())
tree_dict = defaultdict(list)

for _ in range(N):
    root, left, right = list(input().split())
    tree_dict[root] = [left, right]

def preorder(node="A"):
    result = ""
    stack = [node]
    while stack:
        node = stack.pop()
        if node != ".":
            result += node
            right, left = tree_dict[node][1], tree_dict[node][0]
            if right != ".":
                stack.append(right)
            if left != ".":
                stack.append(left)
    print(result)

def inorder(node="A"):
    result = ""
    stack = []
    while stack or node != ".":
        if node != ".":
            stack.append(node)
            node = tree_dict[node][0]
        else:
            if not stack:
                break
            node = stack.pop()
            result += node
            node = tree_dict[node][1]
    print(result)

def postorder(node="A"):
    result = ""
    stack1 = [node]
    stack2 = []
    while stack1:
        node = stack1.pop()
        if node != ".":
            stack2.append(node)
            left, right = tree_dict[node][0], tree_dict[node][1]
            if left != ".":
                stack1.append(left)
            if right != ".":
                stack1.append(right)
    while stack2:
        result += stack2.pop()
    print(result)

preorder()
inorder()
postorder()

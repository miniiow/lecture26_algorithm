# 이진트리를 입력받아, 전위순회, 중위순회, 후위순회한 결과를 출력

def make_tree():
    tree = {}
    tree['A'] = ['B','C']
    tree['B'] = ['D', None]
    tree['C'] = ['E','F']
    tree['D'] = [None, None]
    tree['E'] = [None, None]
    tree['F'] = [None, 'G']
    tree['G'] = [None, None]

    return tree

tree = make_tree()

# 전위순회 preorder
def preorder(tree, n):
    if n is None:
        return
    print(n, end=' ')
    preorder(tree, tree[n][0])
    preorder(tree, tree[n][1])
print('전위순회 : ', end='')
preorder(tree, 'A')
print()

# 중위순회 inorder
def inorder(tree, n):
    if n is None:
        return
    inorder(tree, tree[n][0])
    print(n, end=' ')
    inorder(tree, tree[n][1])
print('중위순회 : ', end='')
inorder(tree, 'A')
print()

# 후위순회 postorder
def postorder(tree, n):
    if n is None :
        return
    postorder(tree, tree[n][0])
    postorder(tree, tree[n][1])
    print(n, end=' ')
print('후위순회 : ', end='')
postorder(tree, 'A')
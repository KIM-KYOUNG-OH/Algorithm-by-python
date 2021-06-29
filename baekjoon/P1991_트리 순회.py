import sys


def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(edges[node][0])
        preorder(edges[node][1])


def inorder(node):
    if node != '.':
        inorder(edges[node][0])
        print(node, end='')
        inorder(edges[node][1])


def postorder(node):
    if node != '.':
        postorder(edges[node][0])
        postorder(edges[node][1])
        print(node, end='')


n = int(sys.stdin.readline().rstrip())
edges = dict()
for i in range(n):
    parent, left_child, right_child = sys.stdin.readline().rstrip().split()
    edges[parent] = [left_child, right_child]
preorder('A')
print()
inorder('A')
print()
postorder('A')

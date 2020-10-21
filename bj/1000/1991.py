from sys import stdin

def preorder(tree, node):
    print(node.item, end='')
    if node.lchild != '.':
        preorder(tree, tree[node.lchild])
    if node.rchild != '.':
        preorder(tree, tree[node.rchild])


def inorder(tree, node):
    if node.lchild != '.':
        inorder(tree, tree[node.lchild])
    print(node.item, end='')
    if node.rchild != '.':
        inorder(tree, tree[node.rchild])


def postorder(tree, node):
    if node.lchild != '.':
        postorder(tree, tree[node.lchild])
    if node.rchild != '.':
        postorder(tree, tree[node.rchild])
    print(node.item, end='')


class Node:
    def __init__(self, item, lchild, rchild):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild


def solve():
    N = int(input())
    tree = dict()
    for i in range(N):
        p, l, r = list(map(str, stdin.readline().split()))
        tree[p] = Node(p, l, r)
    preorder(tree, tree['A'])
    print()
    inorder(tree, tree['A'])
    print()
    postorder(tree, tree['A'])


if __name__ == '__main__':
    solve()

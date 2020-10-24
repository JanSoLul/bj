from sys import stdin, setrecursionlimit
read = lambda : stdin.readline()
setrecursionlimit(10**4*2)

def solve():
    class Node:
        def __init__(self, key):
            self.key = key
            self.lchild = None
            self.rchild = None

        def __str__(self):
            return str(self.key)

    class BinarySearchTree:
        def __init__(self):
            self.root = None

        def insert(self, key):
            if self.root == None:
                self.root = Node(key)
            else:
                current = self.root
                while True:
                    if current.key > key:
                        if current.lchild == None:
                            current.lchild = Node(key)
                            break
                        current = current.lchild
                    elif current.key < key:
                        if current.rchild == None:
                            current.rchild = Node(key)
                            break
                        current = current.rchild

        def postorder(self, node):
            if node.lchild != None:
                self.postorder(node.lchild)
            if node.rchild != None:
                self.postorder(node.rchild)
            print(node)

    bt = BinarySearchTree()
    while True:
        try:
            bt.insert(int(read()))
        except:
            break
    bt.postorder(bt.root)


if __name__ == "__main__":
    solve()

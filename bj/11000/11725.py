from sys import stdin
from collections import deque

def solve():
    N = int(stdin.readline())
    head = [0 for _ in range(N+1)]
    head[1] = 1

    tree = [[] for _ in range(N+1)]

    for _ in range(N-1):
        x, y = list(map(int, stdin.readline().split()))
        tree[x].append(y)
        tree[y].append(x)

    q = deque()
    q.append(1)
    while q:
        node = q.popleft()
        for child in tree[node]:
            if not head[child]:
                head[child] = node
                q.append(child)

    for h in head[2:]:
        print(h)

if __name__ == '__main__':
    solve()

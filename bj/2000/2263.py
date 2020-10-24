from sys import stdin, setrecursionlimit
read = lambda : stdin.readline()
N = int(read())
inorder = list(map(int, read().split()))
postorder = list(map(int, read().split()))


def cal(position, in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:  return
    root = postorder[post_end]
    print(root, end=' ')
    p = position[root]
    left = p - in_start
    cal(position, in_start, p-1, post_start, post_start+left-1)
    cal(position, p+1, in_end, post_start+left, post_end-1)


def solve():
    position = {}
    for i in range(N):
        position[inorder[i]] = i
    cal(position, 0, N-1, 0, N-1)


if __name__ == '__main__':
    setrecursionlimit(10**7)
    solve()


from sys import stdin
from collections import deque
read = lambda : stdin.readline()

def solve():
    N, M = list(map(int, read().split()))
    B = [read()[:-1] for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]

    def move(x, y, dx, dy):
        count = 0
        while B[x+dx][y+dy] != '#' and B[x][y] != 'O':
            x += dx
            y += dy
            count += 1
        return x, y, count

    def bfs():
        rx, ry, bx, by = 0, 0, 0, 0
        for i in range(N):
            for j in range(M):
                if B[i][j] == 'R':
                    rx, ry = i, j
                elif B[i][j] == 'B':
                    bx, by = i, j
        queue.append((rx, ry, bx, by, 1))
        visited[rx][ry][bx][by] = True
        while queue:
            rx, ry, bx, by, count = queue.popleft()
            if count > 10:
                break
            for i in range(4):
                nrx, nry, nrcnt = move(rx, ry, dx[i], dy[i])
                nbx, nby, nbcnt = move(bx, by, dx[i], dy[i])
                if B[nbx][nby] != 'O':
                    if B[nrx][nry] == 'O':
                        print(count)
                        return
                    if nrx == nbx and nry == nby:
                        if nrcnt > nbcnt:
                            nrx -= dx[i]
                            nry -= dy[i]
                        else:
                            nbx -= dx[i]
                            nby -= dy[i]
                    if not visited[nrx][nry][nbx][nby]:
                        visited[nrx][nry][nbx][nby] = True
                        queue.append((nrx, nry, nbx, nby, count+1))
        print(-1)


    bfs()


if __name__ == '__main__':
    solve()

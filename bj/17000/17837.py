from sys import stdin
from collections import deque
read = lambda : stdin.readline()

def solve():
    N, K = map(int, read().split())
    mapL = []
    piece = []
    pos = [[deque() for _ in range(N)] for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for _ in range(N):
        mapL.append(list(map(int, read().split())))
    for i in range(K):
        x, y, direction = map(int, read().split())
        x -= 1
        y -= 1
        piece.append([x, y, direction-1])
        pos[x][y].append(i)

    turn = 0
    while True:
        turn += 1
        if turn > 1000:
            print(-1)
            return
        for i in range(K):
            cx, cy, direction = piece[i]
            nx = cx + dx[direction]
            ny = cy + dy[direction]
            if 0>nx or nx>=N or 0>ny or ny>=N or mapL[nx][ny]==2:
                if direction==0 or direction==2:
                    direction += 1
                else:
                    direction -= 1
                piece[i][2] = direction
                nx = cx + dx[direction]
                ny = cy + dy[direction]
            if 0>nx or nx>=N or 0>ny or ny>=N or mapL[nx][ny]==2:
                continue
            elif mapL[nx][ny]==0:
                remainL = deque()
                isMove = False
                while pos[cx][cy]:
                    check = pos[cx][cy].popleft()
                    if i==check:
                        isMove = True
                    else:
                        if not isMove:
                            remainL.append(check)
                    if isMove:
                        pos[nx][ny].append(check)
                        piece[check] = [nx, ny, piece[check][2]]
                pos[cx][cy] = remainL
            elif mapL[nx][ny]==1:
                while pos[cx][cy]:
                    check = pos[cx][cy].pop()
                    pos[nx][ny].append(check)
                    piece[check] = [nx, ny, piece[check][2]]
                    if i==check:
                        break
            if len(pos[nx][ny]) >= 4:
                print(turn)
                return


if __name__ == '__main__':
    solve()

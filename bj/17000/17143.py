from sys import stdin
read = lambda : stdin.readline()

def solve():
    R, C, M = map(int, read().split())
    fishing = [[None for _ in range(C)] for _ in range(R)]
    checkL = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    for _ in range(M):
        r, c, s, d, z = map(int, read().split())
        fishing[r-1][c-1] = [s, d-1, z]
    anglerPos = -1
    totalShark = 0
    while True:
        # 낚시왕이 오른쪽으로 한 칸 이동한다.
        anglerPos += 1
        if anglerPos == C:
            break
        # 낚시왕이 있는 열에 있는 상어 중에서 가까운 상어를 잡는다.
        for i in range(R):
            if fishing[i][anglerPos]:
                totalShark += fishing[i][anglerPos][2]
                fishing[i][anglerPos] = None
                break
        # 상어 이동
        AfterMove = []
        for i in range(R):
            for j in range(C):
                if fishing[i][j]:
                    speed, direction, size = fishing[i][j]
                    fishing[i][j] = None
                    nx = i + speed * checkL[direction][0]
                    ny = j + speed * checkL[direction][1]
                    while True:
                        if 0<=nx<R and 0<=ny<C:
                            break
                        if nx < 0:
                            nx = -nx
                            direction = 1
                        elif nx >= R:
                            nx = 2*R -2 -nx
                            direction = 0
                        elif ny < 0:
                            ny = -ny
                            direction = 2
                        elif ny >= C:
                            ny = 2*C -2 - ny
                            direction = 3
                    AfterMove.append((nx, ny, speed, direction, size))
        # 상어 배치
        for cx, cy, speed, direction, size in AfterMove:
            # 같은 칸이면 잡아먹는다
            if fishing[cx][cy]:
                if size > fishing[cx][cy][2]:
                    fishing[cx][cy] = [speed, direction, size]
            else:
                fishing[cx][cy] = [speed, direction, size]
    print(totalShark)


if __name__ == '__main__':
    solve()







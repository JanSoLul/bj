from sys import stdin
read = lambda : stdin.readline()

def solve():
    N, M, K = map(int, read().split())
    check = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    mapL = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        r, c, m, s, d = map(int, read().split())
        r -= 1
        c -= 1
        mapL[r][c].append([m, s, d])
    for _ in range(K):
        save = [[[] for _ in range(N)] for _ in range(N)]
        # fireball 이동
        for i in range(N):
            for j in range(N):
                while mapL[i][j]:
                    m, s, d = mapL[i][j].pop()
                    nx = i + check[d][0]*s
                    ny = j + check[d][1]*s
                    nx %= N
                    ny %= N
                    save[nx][ny].append([m, s, d])
        mapL = save
        # 파이어볼 확인
        for i in range(N):
            for j in range(N):
                countFireball = len(mapL[i][j])
                if countFireball > 1:
                    sumM = 0
                    sumS = 0
                    isEven = True
                    checkingUnion = 0
                    isFirst = True
                    divideFireball = []
                    while mapL[i][j]:
                        m, s, d = mapL[i][j].pop()
                        sumM += m
                        sumS += s
                        if isFirst:
                            isFirst = False
                            if d%2 == 0:
                                isEven = True
                            else:
                                isEven = False
                        elif checkingUnion == 0:
                            if isEven:
                                if d%2 != 0:
                                    checkingUnion = 1
                            else:
                                if d%2 == 0:
                                    checkingUnion = 1
                    sumM //= 5
                    sumS //= countFireball
                    if sumM > 0:
                        for d in range(0, 8, 2):
                            divideFireball.append([sumM, sumS, d+checkingUnion])
                        mapL[i][j] = divideFireball
    # 4. 질량이 0인 파이어볼은 소멸되어 없어진다.
    totalM = 0
    for i in range(N):
        for j in range(N):
            while mapL[i][j]:
                m, dummy1, dummy2 = mapL[i][j].pop()
                totalM += m
    print(totalM)


if __name__ == '__main__':
    solve()

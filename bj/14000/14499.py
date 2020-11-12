from sys import stdin
read = lambda : stdin.readline()

def solve():
    N, M, x, y, K = list(map(int, read().split()))
    mapL = []
    diceLR = [0, 0, 0, 0]
    diceTB = [0, 0, 0, 0]
    for _ in range(N):
        mapL.append(list(map(int, read().split())))
    if K == 1:
        moves = [int(read())]
    else:
        moves = list(map(int, read().split()))
    for move in moves:
        if move == 1:   # 동쪽
            y += 1
            if y == M:
                y -= 1
                continue
            diceLR = [diceLR[-1]] + diceLR[:3]
            if mapL[x][y] != 0:
                diceLR[1] = mapL[x][y]
                mapL[x][y] = 0
            else:
                mapL[x][y] = diceLR[1]
            diceTB[1] = diceLR[1]
            diceTB[3] = diceLR[3]
            print(diceTB[3])
        elif move == 2: # 서쪽
            y -= 1
            if y == -1:
                y += 1
                continue
            diceLR = diceLR[1:] + [diceLR[0]]
            if mapL[x][y] != 0:
                diceLR[1] = mapL[x][y]
                mapL[x][y] = 0
            else:
                mapL[x][y] = diceLR[1]
            diceTB[1] = diceLR[1]
            diceTB[3] = diceLR[3]
            print(diceTB[3])
        elif move == 3: # 북쪽
            x -= 1
            if x == -1:
                x += 1
                continue
            diceTB = diceTB[1:] + [diceTB[0]]
            if mapL[x][y] != 0:
                diceTB[1] = mapL[x][y]
                mapL[x][y] = 0
            else:
                mapL[x][y] = diceTB[1]
            diceLR[1] = diceTB[1]
            diceLR[3] = diceTB[3]
            print(diceLR[3])
        else:   # 남쪽
            x += 1
            if x == N:
                x -= 1
                continue
            diceTB = [diceTB[-1]] + diceTB[:-1]
            if mapL[x][y] != 0:
                diceTB[1] = mapL[x][y]
                mapL[x][y] = 0
            else:
                mapL[x][y] = diceTB[1]
            diceLR[1] = diceTB[1]
            diceLR[3] = diceTB[3]
            print(diceLR[3])


if __name__ == '__main__':
    solve()






from sys import stdin
from copy import deepcopy
read = lambda : stdin.readline()

def solve():
    N, M = map(int, read().split())
    mapL = []
    house = []
    chicken = []
    for i in range(N):
        mapL.append(list(map(int, read().split())))
        for j in range(N):
            if mapL[i][j] == 1:
                house.append((i, j))
            elif mapL[i][j] == 2:
                chicken.append((i, j))

    chickenLen = len(chicken)
    chickenD = [[] for _ in range(chickenLen)]
    houseLen = len(house)
    result = [10 ** 8]
    for hx, hy in house:
        for i in range(chickenLen):
            cx, cy = chicken[i]
            tmpD = abs(hx-cx) + abs(hy-cy)
            chickenD[i].append(tmpD)

    def checkChicken(start, minL, chickenCount):
        if chickenCount == M:
            tmp = sum(minL)
            if result[0] > tmp:
                result[0] = tmp
            return
        for i in range(start, chickenLen):
            if not minL:
                checkChicken(i+1, deepcopy(chickenD[i]), chickenCount+1)
            else:
                tmpMin = deepcopy(minL)
                for j in range(houseLen):
                    tmpMin[j] = min(tmpMin[j], chickenD[i][j])
                checkChicken(i+1, tmpMin, chickenCount+1)

    checkChicken(0, None, 0)
    print(result[0])


if __name__ == '__main__':
    solve()

from sys import stdin

def solve():
    N, M = list(map(int, stdin.readline().split()))
    mapL = []
    cctvL = []
    directionL = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    type15 = [0, 1, 2, 3]
    type2 = [[0, 1], [2, 3]]
    type3 = [[0, 2], [0, 3], [1, 2], [1, 3]]
    type4 = [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
    minNum = [100]
    for i in range(N):
        mapL.append(list(map(int, stdin.readline().split())))
        for j in range(M):
            if mapL[i][j] != 0 and mapL[i][j] != 6:
                cctvL.append((i, j, mapL[i][j]))

    cctvLen = [len(cctvL)]
    def checkSpace():
        count = 0
        for i in range(N):
            for j in range(M):
                if mapL[i][j] == 0:
                    count += 1
        return count


    def monitorSpace(x, y, direction):
        monitorL = []
        addX, addY = directionL[direction]
        nextX = x
        nextY = y
        while True:
            nextX += addX
            nextY += addY
            if 0<=nextX<N and 0<=nextY<M:
                if mapL[nextX][nextY] == 6:
                    return monitorL
                if mapL[nextX][nextY] == 0:
                    monitorL.append((nextX, nextY))
                    mapL[nextX][nextY] = -1
            else:
                return monitorL


    def getBackSpace(monitorL):
        for x, y in monitorL:
            mapL[x][y] = 0


    def setCCTV(index):
        if index == cctvLen[0]:
            tmpCount = checkSpace()
            if minNum[0] > tmpCount:
                minNum[0] = tmpCount
            return
        x, y, num = cctvL[index]
        if num == 1:
            for direction in type15:
                changeL = monitorSpace(x, y, direction)
                setCCTV(index+1)
                getBackSpace(changeL)
        elif num == 2:
            for checkL in type2:
                changeList = []
                for direction in checkL:
                    changeList.append(monitorSpace(x, y, direction))
                setCCTV(index+1)
                for check in changeList:
                    getBackSpace(check)
        elif num == 3:
            for checkL in type3:
                changeList = []
                for direction in checkL:
                    changeList.append(monitorSpace(x, y, direction))
                setCCTV(index+1)
                for check in changeList:
                    getBackSpace(check)
        elif num == 4:
            for checkL in type4:
                changeList = []
                for direction in checkL:
                    changeList.append(monitorSpace(x, y, direction))
                setCCTV(index+1)
                for check in changeList:
                    getBackSpace(check)
        elif num == 5:
            changeList = []
            for direction in type15:
                changeList.append(monitorSpace(x, y, direction))
            setCCTV(index+1)
            for check in changeList:
                getBackSpace(check)
    setCCTV(0)
    print(minNum[0])

if __name__ == '__main__':
    solve()

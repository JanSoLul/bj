from sys import stdin
read = lambda : stdin.readline()

def solve():
    global N
    global L
    N, L = list(map(int, read().split()))
    mapL = []
    for _ in range(N):
        mapL.append(list(map(int, read().split())))

    roadCount = 0
    for i in range(N):
        runwayLength = 0
        isRunway = [False for _ in range(N)]
        for j in range(N):
            if j==0:
                curHeight = mapL[i][j]
            else:
                if curHeight == mapL[i][j]:
                    pass
                elif curHeight - mapL[i][j] == 1:
                    isSuccess = False
                    nextHeight = mapL[i][j]
                    if j+L-1 < N:
                        for k in range(L):
                            if mapL[i][j+k] != nextHeight or isRunway[j+k]:
                                break
                            isRunway[j+k] = True
                            if k==L-1:
                                isSuccess = True
                    if isSuccess:
                        curHeight = nextHeight
                        j += L-1
                    else:
                        break
                elif curHeight - mapL[i][j] == -1:
                    isSuccess = False
                    if j-L >= 0:
                        for k in range(L):
                            if mapL[i][j-k-1] != curHeight or isRunway[j-k-1]:
                                break
                            isRunway[j-k-1] = True
                            if k==L-1:
                                isSuccess = True
                    if isSuccess:
                        curHeight = mapL[i][j]
                    else:
                        break
                else:
                    break
            if j==N-1:
                roadCount += 1
                break
    for j in range(N):
        runwayLength = 0
        isRunway = [False for _ in range(N)]
        for i in range(N):
            if i==0:
                curHeight = mapL[i][j]
            else:
                if curHeight == mapL[i][j]:
                    pass
                elif curHeight - mapL[i][j] == 1:
                    isSuccess = False
                    nextHeight = mapL[i][j]
                    if i+L-1 < N:
                        for k in range(L):
                            if mapL[i+k][j] != nextHeight or isRunway[i+k]:
                                break
                            isRunway[i+k] = True
                            if k==L-1:
                                isSuccess = True
                    if isSuccess:
                        curHeight = nextHeight
                        i += L-1
                    else:
                        break
                elif curHeight - mapL[i][j] == -1:
                    isSuccess = False
                    if i-L >= 0:
                        for k in range(L):
                            if mapL[i-k-1][j] != curHeight or isRunway[i-k-1]:
                                break
                            isRunway[i-k-1] = True
                            if k==L-1:
                                isSuccess = True
                    if isSuccess:
                        curHeight = mapL[i][j]
                    else:
                        break
                else:
                    break
            if i==N-1:
                roadCount += 1
                break

    print(roadCount)


if __name__ == '__main__':
    solve()

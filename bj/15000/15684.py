from sys import stdin
read = lambda : stdin.readline()

def solve():
    M, N, H = list(map(int, read().split()))
    ladder = [[False for _ in range(M-1)] for _ in range(H)]
    checkL = [[0, -1], [0, 1]]
    minResult = [4]
    for _ in range(N):
        tmph, tmpm = list(map(int, read().split()))
        ladder[tmph-1][tmpm-1] = True


    def checkLadderGame():
        for i in range(M):
            curw = i
            curh = 0
            while curh < H:
                if curw < M-1 and ladder[curh][curw]:
                    curw += 1
                elif curw > 0 and ladder[curh][curw-1]:
                    curw -= 1
                curh += 1
            if i != curw:
                return False
        return True


    def setLadder(start, ladderCount):
        if checkLadderGame():
            if minResult[0] > ladderCount:
                minResult[0] = ladderCount
                return
        if ladderCount == 3:
            return
        for ij in range(start, (M-1)*H):
            i = ij // (M-1)
            j = ij % (M-1)
            isPossible = True
            if not ladder[i][j]:
                for addX, addY in checkL:
                    checkX = i + addX
                    checkY = j + addY
                    if 0<=checkX<H and 0<=checkY<M-1:
                        if ladder[checkX][checkY]:
                            isPossible = False
                            break
                if not isPossible:
                    continue
                ladder[i][j] = True
                setLadder(ij+1, ladderCount+1)
                ladder[i][j] = False


    setLadder(0, 0)
    if minResult[0] == 4:
        print(-1)
    else:
        print(minResult[0])






if __name__ == '__main__':
    solve()

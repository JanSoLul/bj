from sys import stdin
from collections import deque
read = lambda : stdin.readline()

def solve():
    gear = [deque() for _ in range(4)]
    for i in range(4):
        tmp = read()[:-1]
        for j in range(8):
            gear[i].append(int(tmp[j]))
    T = int(read())

    def isRotate(gn):
        rotateCheck = [False for _ in range(4)]
        rotateCheck[gn] = True
        leftgn, rightgn = gn-1, gn+1
        while leftgn >= 0:
            if gear[leftgn][2] != gear[leftgn+1][6]:
                rotateCheck[leftgn] = True
                leftgn -= 1
            else:
                break
        while rightgn <= 3:
            if gear[rightgn-1][2] != gear[rightgn][6]:
                rotateCheck[rightgn] = True
                rightgn += 1
            else:
                break
        return rotateCheck

    for _ in range(T):
        gearNum, directionOfRotation = list(map(int, read().split()))
        dorL = [directionOfRotation for _ in range(4)]
        gearNum -= 1
        if gearNum % 2 == 0:
            dorL[1] *= -1
            dorL[3] *= -1
        else:
            dorL[2] *= -1
            dorL[0] *= -1
        rotateCheck = isRotate(gearNum)
        for i in range(4):
            if rotateCheck[i]:
                if dorL[i] == 1:
                    tmp = gear[i].pop()
                    gear[i].appendleft(tmp)
                else:
                    tmp = gear[i].popleft()
                    gear[i].append(tmp)

    result = 0
    for i in range(4):
        if gear[i][0] == 1:
            result += 1 << i
    print(result)





if __name__ == '__main__':
    solve()

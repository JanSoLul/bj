from sys import stdin
from collections import deque
read = lambda : stdin.readline()

def solve():
    N = int(read())
    red = [deque([0 for _ in range(4)]) for _ in range(4)]
    blue = [deque([0 for _ in range(6)]) for _ in range(4)]
    green = [deque([0 for _ in range(6)]) for _ in range(4)]
    partType = [[[0, 0]], [[0, 0], [0, 1]], [[0, 0], [1, 0]]]

    score = [0]

    def move():
        # 파란 보드로 이동
        for i in range(-1, -5, -1):
            target = []
            for j in range(4):
                if red[j][i] > 0:
                    target.append(j)
            for j in range(6):
                if j > 0:
                    isBreak = False
                    for k in target:
                        if blue[k][j]>0:
                            isBreak = True
                            break
                    if isBreak:
                        break
                    for k in target:
                        blue[k][j-1] = 0
                for k in target:
                    blue[k][j] = 1

        # 초록 보드로 이동
        for i in range(-1, -5, -1):
            target = []
            for j in range(4):
                if red[i][j] > 0:
                    target.append(j)
                    red[i][j] = 0
            for j in range(6):
                if j>0:
                    isBreak = False
                    for k in target:
                        if green[k][j]>0:
                            isBreak = True
                            break
                    if isBreak:
                        break
                    for k in target:
                        green[k][j-1] = 0
                for k in target:
                    green[k][j] = 1


    def removeLine():
        rmline = 0
        # 파란 보드 라인 삭제
        for i in range(-1, -5, -1):
            i = i + rmline
            for j in range(4):
                if blue[j][i]==0:
                    break
                if j==3:
                    for k in range(4):
                        save = deque()
                        for l in range(-i):
                            tmp = blue[k].pop()
                            if l!=-i-1:
                                save.appendleft(tmp)
                        blue[k].appendleft(0)
                        blue[k].extend(save)
                    rmline += 1
                    score[0] += 1
        rmline = 0
        # 초록 보드 라인 삭제
        for i in range(-1, -5, -1):
            i = i + rmline
            for j in range(4):
                if green[j][i]==0:
                    break
                if j==3:
                    for k in range(4):
                        save = deque()
                        for l in range(-i):
                            tmp = green[k].pop()
                            if l!=-i-1:
                                save.appendleft(tmp)
                        green[k].appendleft(0)
                        green[k].extend(save)
                    rmline += 1
                    score[0] += 1


    # 라인 넘어가면 맨 뒷줄 삭제후 한 줄씩 민다
    def limitLine():
        for i in range(2):
            isCheck = False
            for j in range(4):
                if blue[j][i]==1:
                    isCheck = True
                if isCheck:
                    for k in range(4):
                        blue[k].pop()
                        blue[k].appendleft(0)
                    break
            isCheck = False
            for j in range(4):
                if green[j][i]==1:
                    isCheck = True
                if isCheck:
                    for k in range(4):
                        green[k].pop()
                        green[k].appendleft(0)
                    break


    for _ in range(N):
        t, x, y = map(int, read().split())
        for tx, ty in partType[t-1]:
            rx, ry = x+tx, y+ty
            red[rx][ry] = 1
        '''
        print('red')
        for i in range(4):
            print(red[i])
        '''
        move()
        removeLine()
        limitLine()
        '''
        print('blue')
        for i in range(4):
            print(blue[i])
        print('green')
        for i in range(6):
            for j in range(4):
                print(green[j][i], end=' ')
            print()
        '''
    print(score[0])
    sumBlock = 0
    for i in range(4):
        sumBlock += sum(blue[i])
        sumBlock += sum(green[i])
    print(sumBlock)


if __name__ == '__main__':
    solve()

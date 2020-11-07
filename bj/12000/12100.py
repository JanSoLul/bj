from sys import stdin
from copy import deepcopy
read = lambda : stdin.readline()

def solve():
    N = int(read())
    maps = [list(map(int, read().split())) for _ in range(N)]

    def right(tmpmap):
        for i in range(N):
            save = -1
            saveL = []
            for j in range(N-1, -1, -1):
                if tmpmap[i][j] != 0:
                    if tmpmap[i][j] == save:
                        saveL.append(save*2)
                        save = -1
                    else:
                        if save != -1:
                            saveL.append(save)
                        save = tmpmap[i][j]
                        if j==0:
                            saveL.append(save)
                    tmpmap[i][j] = 0
                else:
                    if j==0 and save!=-1:
                        saveL.append(save)
            count = -1
            for j in saveL:
                tmpmap[i][count] = j
                count -= 1
        return tmpmap


    def left(tmpmap):
        for i in range(N):
            save = -1
            saveL = []
            for j in range(N):
                if tmpmap[i][j] != 0:
                    if tmpmap[i][j] == save:
                        saveL.append(save*2)
                        save = -1
                    else:
                        if save != -1:
                            saveL.append(save)
                        save = tmpmap[i][j]
                        if j == N-1:
                            saveL.append(save)
                    tmpmap[i][j] = 0
                else:
                    if j==N-1 and save!=-1:
                        saveL.append(save)
            count = 0
            for j in saveL:
                tmpmap[i][count] = j
                count += 1
        return tmpmap


    def up(tmpmap):
        for i in range(N):
            save = -1
            saveL = []
            for j in range(N):
                if tmpmap[j][i] != 0:
                    if tmpmap[j][i] == save:
                        saveL.append(save*2)
                        save = -1
                    else:
                        if save != -1:
                            saveL.append(save)
                        save = tmpmap[j][i]
                        if j == N-1:
                            saveL.append(save)
                    tmpmap[j][i] = 0
                else:
                    if j==N-1 and save != -1:
                        saveL.append(save)
            count = 0
            for j in saveL:
                tmpmap[count][i] = j
                count += 1
        return tmpmap


    def down(tmpmap):
        for i in range(N):
            save = -1
            saveL = []
            for j in range(N-1, -1, -1):
                if tmpmap[j][i] != 0:
                    if tmpmap[j][i] == save:
                        saveL.append(save*2)
                        save = -1
                    else:
                        if save != -1:
                            saveL.append(save)
                        save = tmpmap[j][i]
                        if j == 0:
                            saveL.append(save)
                    tmpmap[j][i] = 0
                else:
                    if j==0 and save!=-1:
                        saveL.append(save)
            count = -1
            for j in saveL:
                tmpmap[count][i] = j
                count -= 1
        return tmpmap

    maxNum = [0]
    def move(tmpmap, count):
        if count > 5:
            for i in range(N):
                tmpMax = max(tmpmap[i])
                if tmpMax > maxNum[0]:
                    maxNum[0] = tmpMax
        else:
            nextmap = left(deepcopy(tmpmap))
            move(nextmap, count+1)
            nextmap = right(deepcopy(tmpmap))
            move(nextmap, count+1)
            nextmap = up(deepcopy(tmpmap))
            move(nextmap, count+1)
            nextmap = down(deepcopy(tmpmap))
            move(nextmap, count+1)

    move(maps, 1)
    print(maxNum[0])


if __name__ == '__main__':
    solve()

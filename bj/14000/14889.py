from sys import stdin

N = int(input())
abilityL = [list(map(int, stdin.readline().split())) for _ in range(N)]
wholeL = [i for i in range(1, N+1)]
startL = []
linkL = []
diffMin = 100
count = 0

def selStart(arg):
    global count
    global diffMin
    if count == N/2:
        linkL = wholeL[:]
        linkSynergy = calSynergy(linkL)
        startSynergy = calSynergy(startL)
        tmpdiff = abs(linkSynergy - startSynergy)
        if diffMin > tmpdiff:
            diffMin = tmpdiff
    elif arg == N:
        return 0
    else:
        startL.append(arg)
        wholeL.remove(arg)
        count += 1
        selStart(arg+1)
        count -= 1
        startL.remove(arg)
        wholeL.append(arg)
        selStart(arg+1)


def calSynergy(tmpL):
    synergyCount = 0
    for i in tmpL:
        for j in tmpL:
            if i != j:
                synergyCount += abilityL[i-1][j-1]
    return synergyCount


selStart(1)
print(diffMin)

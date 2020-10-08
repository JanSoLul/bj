N, M = list(map(int, input().split()))
numList = []


def nextNum(arg):
    if arg == M:
        for i in numList:
            print(i, end=' ')
        print()
    else:
        for i in range(numList[-1], N+1):
            numList.append(i)
            nextNum(arg+1)
            numList.pop()


for i in range(1, N+1):
    numList.append(i)
    nextNum(1)
    numList.pop()

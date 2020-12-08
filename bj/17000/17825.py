from sys import stdin
from collections import deque
read = lambda : stdin.readline()

class Node:
    def __init__(self, num):
        self.num = num
        self.shortcut = None
        self.next = None


    def addNext(self, nextNode):
        self.next = nextNode


    def addShortcut(self, shortcut):
        self.shortcut = shortcut


def solve():
    dice = list(map(int, read().split()))
    # Map Initialize
    mapL = []
    prev = None
    head = None
    tail = None
    shortPrevs = []
    shortTail = None
    for i in range(22):
        new = Node(i*2)
        if i==0:
            head = new
        else:
            prev.addNext(new)
            if i==5:
                for j in range(1, 4):
                    new2 = Node(10+j*3)
                    if j==1:
                        new.addShortcut(new2)
                    else:
                        prev.addNext(new2)
                        if j==3:
                            shortPrevs.append(new2)
                    prev = new2
            elif i==10:
                for j in range(1, 3):
                    new2 = Node(20+j*2)
                    if j==1:
                        new.addShortcut(new2)
                    else:
                        prev.addNext(new2)
                        if j==2:
                            shortPrevs.append(new2)
                    prev = new2
            elif i==15:
                for j in range(1, 4):
                    new2 = Node(30-j-1)
                    if j==1:
                        new.addShortcut(new2)
                    else:
                        prev.addNext(new2)
                        if j==3:
                            shortPrevs.append(new2)
                    prev = new2
            elif i==20:
                shortTail = new
            elif i==21:
                new = Node(0)
                prev.addNext(new)
                tail = new
        prev = new
    for i in range(3):
        new = Node(25+i*5)
        if i == 0:
            for j in shortPrevs:
                j.addNext(new)
        else:
            prev.addNext(new)
            if i==2:
                new.addNext(shortTail)
        prev = new

    run = [head for _ in range(4)]

    def move(allRun, target, moveCount):
        nextRun = allRun[target]
        isTail = False
        for i in range(moveCount):
            if i==0:
                if nextRun.shortcut:
                    nextRun = nextRun.shortcut
                    continue
            nextRun = nextRun.next
            if tail==nextRun:
                return tail
        isExist = False
        for check in allRun:
            if check==nextRun:
                isExist = True
                break
        if isExist:
            return None
        return nextRun


    maxNum = [0]
    q = deque()
    q.append((0, run, 0))
    while q:
        index, cr, count = q.popleft()
        if index == 10:
            maxNum[0] = max(maxNum[0], count)
            continue
        isNew = False
        for i in range(4):
            if isNew:
                break
            if cr[i]==head:
                isNew = True
            if cr[i]==tail:
                continue
            afterMove = move(cr, i, dice[index])
            if afterMove:
                copyRun = [cr[i] for i in range(4)]
                copyRun[i] = afterMove
                q.append((index+1, copyRun, count+afterMove.num))


    print(maxNum[0])


if __name__ == '__main__':
    solve()

from sys import stdin
read = lambda : stdin.readline()


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isApple = False
        self.isSnake = False
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self, start):
        dummy = Node(-1, -1)
        self.head = dummy
        start.isSnake = True
        start.prev = self.head
        self.head.next = start
        self.tail = start



    def plusHead(self, newHead):
        newHead.isSnake = True
        newHead.prev = self.head
        tmpNode = self.head.next
        tmpNode.prev = newHead
        newHead.next = tmpNode
        self.head.next = newHead


    def removeTail(self):
        tmpNode = self.tail.prev
        tmpNode.next = None
        self.tail.isSnake = False
        self.tail = tmpNode


def solve():
    N = int(read())
    head = [1, 1]
    lastBody = [1, 1]
    tail = [1, 1]
    Nodes = [[Node(i, j) for j in range(N+1)] for i in range(N+1)]
    apple = int(read())
    for _ in range(apple):
        x, y = list(map(int, read().split()))
        Nodes[x][y].isApple = True
    moveCount = int(read())
    moves = []
    for _ in range(moveCount):
        count, direction = list(map(str, read().split()))
        count = int(count)
        moves.append((count, direction))
    curMoves = 0
    curDirection = 0 # 0:right, 1:down, 2:left, 3:up
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    times = 0
    movesLen = len(moves)
    ll = LinkedList(Nodes[1][1])
    allTime = 0
    timesAfter = 0
    while True:
        eatApple = False
        if times == 0:
            if curMoves < movesLen:
                timesAfter, nextDirection = moves[curMoves]
                timesAfter -= allTime
                curMoves += 1
            else:
                timesAfter = 200
        headX, headY = ll.head.next.x, ll.head.next.y
        headX += directions[curDirection][0]
        headY += directions[curDirection][1]
        times += 1
        allTime += 1
        if headX==0 or headX==N+1 or headY==0 or headY==N+1 or Nodes[headX][headY].isSnake:
            print(allTime)
            break
        if Nodes[headX][headY].isApple:
            eatApple = True
            Nodes[headX][headY].isApple = False
        ll.plusHead(Nodes[headX][headY])
        if not eatApple:
            ll.removeTail()
        if times == timesAfter:
            times = 0
            if nextDirection == 'L':
                curDirection -= 1
                if curDirection < 0:
                    curDirection = 3
            elif nextDirection == 'D':
                curDirection += 1
                if curDirection > 3:
                    curDirection = 0


if __name__ == '__main__':
    solve()

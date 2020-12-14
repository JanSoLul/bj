from sys import stdin
from collections import deque
read = lambda : stdin.readline()

def solve():
    N, K = map(int, read().split())
    tmp = list(map(int, read().split()))
    conveyor = [deque(tmp[:N]), deque(reversed(tmp[N:]))]
    isRobot = [False for _ in range(N)]
    robots = [deque()]
    checkZero = [0]
    step = 0


    # 컨베이어 벨트 회전
    def rotate():
        conveyor[0].appendleft(conveyor[1].popleft())
        conveyor[1].append(conveyor[0].pop())
        newRobot = deque()
        while robots[0]:
            tmp = robots[0].popleft()
            isRobot[tmp] = False
            tmp += 1
            if tmp == N-1:
                continue
            isRobot[tmp] = True
            newRobot.append(tmp)
        robots[0] = newRobot


    # 로봇 이동
    def move():
        newRobot = deque()
        while robots[0]:
            cy = robots[0].popleft()
            isRobot[cy] = False
            cy += 1
            if conveyor[0][cy] == 0 or isRobot[cy]:
                cy -= 1
            else:
                conveyor[0][cy] -= 1
                zeroCheck(0, cy)
                if cy == N-1:
                    continue
            isRobot[cy] = True
            newRobot.append(cy)
        robots[0] = newRobot


    # 내구도 0인지 체크
    def zeroCheck(x, y):
        if conveyor[x][y] == 0:
            checkZero[0] += 1


    while True:
        step += 1
        rotate()
        move()
        if conveyor[0][0] > 0:
            conveyor[0][0] -= 1
            zeroCheck(0, 0)
            isRobot[0] = True
            robots[0].append(0)
        if checkZero[0] >= K:
            print(step)
            exit(0)


if __name__ == '__main__':
    solve()

from sys import stdin
read = lambda : stdin.readline()

def solve():
    N = int(read())
    checkL = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    location = [[0 for _ in range(101)] for _ in range(101)]
    for _ in range(N):
        x, y, d, g = map(int, read().split())
        location[x][y] = 1
        move = [d]
        for _ in range(g):
            tmp = []
            for i in range(len(move)):
                tmp.append((move[-i-1] +1) % 4)
            move.extend(tmp)
        for i in move:
            nextX = x + checkL[i][0]
            nextY = y + checkL[i][1]
            location[nextX][nextY] = 1
            x, y = nextX, nextY

    result = 0
    for i in range(100):
        for j in range(100):
            if location[i][j]:
                if location[i+1][j] and location[i][j+1] and location[i+1][j+1]:
                    result += 1
    print(result)


if __name__ == '__main__':
    solve()

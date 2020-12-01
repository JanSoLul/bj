from sys import stdin
read = lambda : stdin.readline()

def solve():
    R, C, K = map(int, read().split())
    R -= 1
    C -= 1
    A = []
    for _ in range(3):
        A.append(list(map(int, read().split())))
    r, c = 3, 3
    for i in range(0, 101):
        if R<r and C<c:
            if A[R][C] == K:
                print(i)
                return
        if r >= c:
            maxC = 0
            for j in range(r):
                count = [[0, k] for k in range(101)]
                for k in range(c):
                    if A[j][k] > 0:
                        count[A[j][k]][0] += 1
                count = sorted(count, key = lambda x : (x[0], x[1]))
                A[j] = []
                for cnt, num in count:
                    if cnt > 0:
                        A[j].append(num)
                        A[j].append(cnt)
                if len(A[j]) > maxC:
                    maxC = len(A[j])
            c = maxC
            if c > 100:
                c = 100
            for j in range(r):
                cLen = len(A[j])
                for _ in range(c-cLen):
                    A[j].append(0)
        else:
            maxR = 0
            for j in range(c):
                count = [[0, k] for k in range(101)]
                for k in range(r):
                    if A[k][j] > 0:
                        count[A[k][j]][0] += 1
                        A[k][j] = 0
                count = sorted(count, key = lambda x : (x[0], x[1]))
                tmpSave = []
                for cnt, num in count:
                    if cnt > 0:
                        tmpSave.append(num)
                        tmpSave.append(cnt)
                tmpLen = len(tmpSave)
                if tmpLen > maxR:
                    maxR = tmpLen
                for k in range(tmpLen-len(A)):
                    A.append([0 for _ in range(c)])
                for k in range(tmpLen):
                    A[k][j] = tmpSave[k]
            r = maxR
            if r > 100:
                r = 100
    print(-1)


if __name__ == '__main__':
    solve()

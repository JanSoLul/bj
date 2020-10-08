from sys import stdin

N = int(stdin.readline())
saveTime = []
tmpMax = 0
for i in range(N):
    start, end = list(map(int, stdin.readline().split()))
    if end > tmpMax:
        tmpMax = end + 1
    saveTime.append([start, end])

sortTime = sorted(saveTime, key = lambda x : (x[1], x[0])) #x[1]을 기준으로 오름차순으로 정렬하고
                                                           #두번째 key로 x[0]을 기준으로 오름차순으로 정렬한다.
cur = 0
count = 0
for i in sortTime:
    if cur <= i[0]:
        count += 1
        cur = i[1]
print(count)

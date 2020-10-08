N = int(input())
timeList = list(map(int, input().split()))
sortTime = sorted(timeList)
waitTime = 0
for i in range(N):
    tmp = sortTime[i]
    sortTime[i] += waitTime
    waitTime += tmp
print(sum(sortTime))

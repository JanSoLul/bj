from sys import stdin
K, N = list(map(int, stdin.readline().split()))
lanL = [int(stdin.readline()) for _ in range(K)]
lanL.sort()
left = 0
right = lanL[-1]
saveNum = 0


def calLanCount(num):
    count = 0
    if num != 0:
        for i in lanL:
            count += i // num
        return count
    return N


while left <= right:
    mid = (left + right) // 2
    tmpCount = calLanCount(mid)
    if tmpCount >= N:
        saveNum = mid
        left = mid+1
    else:
        right = mid-1
print(saveNum)



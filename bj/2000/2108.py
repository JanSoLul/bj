from sys import stdin
N = int(stdin.readline())
numL = []
numD = dict()
minNum = 4000
maxNum = -4000
for i in range(N):
    tmp = int(stdin.readline())
    numL.append(tmp)
    if tmp in numD:
        numD[tmp] += 1
    else:
        numD[tmp] = 1
    if tmp > maxNum:
        maxNum = tmp
    if tmp < minNum:
        minNum = tmp


def merge_sort(arr):
    def mSort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        mSort(low, mid)
        mSort(mid, high)
        return merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1

        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]


    return mSort(0, len(arr))

isMinus = False
avg = sum(numL) / N
if avg < 0:
    isMinus = True
    avg = -avg
tmp = int(avg)
if avg - tmp >= 0.5:
    avg = tmp + 1
else:
    avg = tmp
if isMinus:
    avg = -avg
print(avg)
sortL = numL[:]
merge_sort(sortL)
if N%2 == 0:
    midNum = sortL[int(N/2)-1]
else:
    midNum = sortL[N//2]
print(midNum)
mode = []
countMax = 0
for key in numD:
    if numD[key] > countMax:
        mode = [key]
        countMax = numD[key]
    elif numD[key] == countMax:
        mode.append(key)
merge_sort(mode)
if len(mode) == 1:
    print(mode[0])
else:
    print(mode[1])
print(maxNum - minNum)

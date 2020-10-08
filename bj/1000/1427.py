N = input()
numL = []
for i in range(len(N)):
    numL.append(int(N[i]))

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

merge_sort(numL)
for i in range(1, len(numL)+1):
    print(numL[-i], end='')

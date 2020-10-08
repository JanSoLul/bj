import random
import time

def quick_sort(arr):
    def qSort(low, high):
        if high <= low:
            return
        mid = partition(low, high)
        qSort(low, mid-1)
        qSort(mid, high)
        return arr

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return qSort(0, len(arr) - 1)


a = random.sample(range(1, 1000000), 100000)
start = time.time()

a = quick_sort(a)

diffTime = time.time() - start
print(a)
print(diffTime)

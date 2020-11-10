from sys import stdin
read = lambda : stdin.readline()

def solve():
    N = int(read())
    if N == 1:
        tmp = int(read())
        num = [tmp]
    else:
        num = list(map(int, read().split()))
    A, B = list(map(int, read().split()))
    allRet = 0
    for i in num:
        i -= A
        count = 1
        if i <= 0:
            allRet += 1
        else:
            ret = i // B + 1
            if i%B != 0:
                ret += 1
            allRet += ret
    print(allRet)


if __name__ == '__main__':
    solve()

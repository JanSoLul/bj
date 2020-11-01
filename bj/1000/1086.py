from math import factorial, gcd
from sys import stdin
read = lambda : stdin.readline()

def solve():
    N = int(read())
    num = []
    num_len = []
    for i in range(N):
        tmp = read()[:-1]
        num.append(int(tmp))
        num_len.append(len(tmp))
    K = int(read())
    full = (1<<N)-1
    # full : 모든 비트를 1로 설정한 값
    each_bit = [(1<<i) for i in range(N)]
    # each_bit : 각각의 비트의 위치에 바로 접근하기 위한 수를 저장
    lenL = sum(num_len)
    remain = [[0 for _ in range(lenL)] for _ in range(N)]
    # remain : 주어진 숫자의 위치에 따라 나머지를 구하는 리스트
    for i in range(N):
        mx = lenL - num_len[i]
        for j in range(mx+1):
            remain[i][j] = num[i]*(10**(mx-j))%K
    dp = [[-1 for _ in range(full+1)] for _ in range(100)]
    # dp : 첫번째 index는 현재까지 계산된 나머지 값, 두번째 index는 현재까지 진행한 비트

    def cal(length, bit, rm):
        if bit == full:
            return rm==0
        if dp[rm][bit] != -1:
            return dp[rm][bit]
        dp[rm][bit] = 0
        for n in range(N):
            if not bit & each_bit[n]:
                dp[rm][bit] += cal(length+num_len[n], bit|each_bit[n], (rm+remain[n][length])%K)
        return dp[rm][bit]
    ret = cal(0, 0, 0)
    fact = factorial(N)
    g = gcd(ret, fact)
    if ret==0:
        print('0/1')
    else:
        print('%d/%d'%(ret//g, fact//g))


if __name__ == '__main__':
    solve()

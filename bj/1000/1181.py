from sys import stdin, stdout

N = int(stdin.readline())
strL = [stdin.readline()[:-1] for _ in range(N)]
strL = list(set(strL))
strL.sort(key = lambda x : (len(x), x))
for i in strL:
    stdout.write(i + '\n')

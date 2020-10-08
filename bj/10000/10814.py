from sys import stdin, stdout
N = int(stdin.readline())
memberL = []
for i in range(N):
    age, name = list(map(str, stdin.readline().split()))
    age = int(age)
    memberL.append([age, name, i])
memberL.sort(key = lambda x : (x[0], x[2]))
for i in memberL:
    stdout.write(str(i[0]) + ' ' + i[1] + '\n')

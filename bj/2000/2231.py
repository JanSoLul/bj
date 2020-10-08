N = int(input())
isConstructor = False
for i in range(1, N):
    tmp = str(i)
    SSum = i
    for j in tmp:
        SSum += int(j)
    if SSum == N:
        print(i)
        isConstructor = True
        break
if not isConstructor:
    print('0')

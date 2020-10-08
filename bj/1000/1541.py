from sys import stdin
statement = stdin.readline()
minusSplit = statement[:-1].split('-')
plusSplit = []
secretNum = 0
for i in minusSplit:
    plusSplit.append(i.split('+'))
for i in range(len(plusSplit)):
    if i > 0 and len(plusSplit[i]) == 1:
        secretNum -= int(plusSplit[i][0])
    elif i == 0:
        for j in plusSplit[i]:
            secretNum += int(j)
    else:
        for j in plusSplit[i]:
            secretNum -= int(j)
print(secretNum)

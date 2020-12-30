from sys import stdin
from copy import deepcopy
read = lambda : stdin.readline()

def solve():
    N = int(read())
    tmpEquation = read()[:-1]
    numL = []
    opL = []
    maxNum = [-10 ** 10]
    for i in range(N):
        if i%2 == 0:
            numL.append(int(tmpEquation[i]))
        else:
            opL.append(tmpEquation[i])
    lenOP = len(opL)


    def setBracket(isBracket, start):
        if start==lenOP:
            remainNum, remainOP = removeBracket(isBracket)
            ret = remainNum[0]
            for i in range(len(remainOP)):
                ret = calOP(ret, remainNum[i+1], remainOP[i])
            if ret > maxNum[0]:
                maxNum[0] = ret
                return
        for i in range(start, lenOP):
            check = deepcopy(isBracket)
            if i==0 or (i>0 and not check[i-1]):
                check[i] = True
            setBracket(check, i+1)
            setBracket(deepcopy(isBracket), i+1)


    def removeBracket(isBracket):
        remainNum = []
        remainOP = []
        checkBracket = False
        for i in range(lenOP):
            if checkBracket:
                remainOP.append(opL[i])
                checkBracket = False
            elif isBracket[i]:
                remainNum.append(calOP(numL[i], numL[i+1], opL[i]))
                checkBracket  = True
            else:
                remainNum.append(numL[i])
                remainOP.append(opL[i])
        if not checkBracket:
            remainNum.append(numL[-1])
        return (remainNum, remainOP)


    def calOP(num1, num2, op):
        if op == '+':
            return num1+num2
        elif op == '-':
            return num1-num2
        else:
            return num1*num2


    isBracket = [False for _ in range(lenOP)]
    setBracket(isBracket, 0)
    print(maxNum[0])


if __name__ == '__main__':
    solve()

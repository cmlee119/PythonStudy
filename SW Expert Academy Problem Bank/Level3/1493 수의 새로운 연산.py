import sys

sys.stdin = open("SW Expert Academy Problem Bank/Level3/1493 수의 새로운 연산.txt", "r")

def findIndex(num):
    leftTop = rightBottom = 1
    countNum = 1
    while num > rightBottom:
        leftTop = rightBottom + 1
        rightBottom = leftTop + countNum
        countNum += 1

    X = num - leftTop + 1
    Y = countNum - X + 1
    return X, Y

def getValue(X, Y):
    lineNum = X + Y - 1
    leftTop = 1
    for i in range(1, lineNum):
        leftTop += i

    leftTop += X - 1
    return leftTop

def myFunc(p, q):
    X1, Y1 = findIndex(p)
    X2, Y2 = findIndex(q)
    return getValue(X1 + X2, Y1 + Y2)

T = int(input())
for test_case in range(1, T + 1):
    p, q = tuple(int(i) for i in input().split())
    result = myFunc(p, q)
    print(f"#{test_case} {result}")
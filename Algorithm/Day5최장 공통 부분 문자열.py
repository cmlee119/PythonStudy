import sys
sys.stdin = open("./Algorithm/Day5최장 공통 부분 문자열.txt", "r")

def myFunc(strA, i, strB, j):
    if i >= len(strA) or j >= len(strB):
        return 0

    if strA[i] == strB[j]:
        return 1 + myFunc(strA, i + 1, strB, j + 1)

    return max(myFunc(strA, i + 1, strB, j), myFunc(strA, i, strB, j + 1))

T = int(input())
for test_case in range(1, T + 1):
    strA = input()
    strB = input()

    matData = [[0] * len(strB) for _ in range(len(strA))]

    for i in range(0, len(strA)):
        for j in range(0, len(strB)):
            if strA[i] == strB[j]:
                DP =  matData[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0
                matData[i][j] = 1 + DP
            else:
                DP_U = matData[i - 1][j] if i - 1 >= 0 else 0
                DP_L = matData[i][j - 1] if j - 1 >= 0 else 0
                matData[i][j] =  max(DP_U, DP_L)

    print(matData[-1][-1])
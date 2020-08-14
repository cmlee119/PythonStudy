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

    for i in range(len(strA) - 1, -1, -1):
        for j in range(len(strB) -1, -1, -1):
            if strA[i] == strB[j]:
                if i + 1 < len(strA) and j + 1 < len(strB):
                    DP =  matData[i + 1][j + 1]
                else:
                    DP = 0
                
                matData[i][j] = 1 + DP

            else:
                if i + 1 < len(strA):
                    DP_i = matData[i + 1][j]
                else:
                    DP_i = 0

                if j + 1 < len(strB):
                    DP_j = matData[i][j + 1]
                else:
                    DP_j = 0

                matData[i][j] =  max(DP_i, DP_j)

    print(matData[0][0])
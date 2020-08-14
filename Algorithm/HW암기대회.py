import sys
sys.stdin = open("./Algorithm/HW암기대회.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = (int(n) for n in input().split())

    matBoard = [[int(n) for n in input().split()] for _ in range(N)]

    matResult = [[0] * M for _ in range(N)]

    for i in range(0, N):
        for j in range(0, M):
            DP_L = matResult[i][j - 1] if j >= 0 else 0
            DP_U = matResult[i - 1][j] if i >= 0 else 0

            matResult[i][j] = matBoard[i][j] + max(DP_L, DP_U)

    print(matResult[-1][-1])
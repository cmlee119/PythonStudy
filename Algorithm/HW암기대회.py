import sys
sys.stdin = open("./Algorithm/HW암기대회.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = (int(n) for n in input().split())

    matBoard = [[int(n) for n in input().split()] for _ in range(N)]

    matResult = [[0] * M for _ in range(N)]

    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            if j + 1 < M:
                DP_R = matResult[i][j + 1]
            else:
                DP_R = 0

            if i + 1 < N:
                DP_D = matResult[i + 1][j]
            else:
                DP_D = 0

            matResult[i][j] = matBoard[i][j] + max(DP_R, DP_D)

    print(matResult[0][0])
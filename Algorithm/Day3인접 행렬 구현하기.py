import sys
sys.stdin = open("./Algorithm/Day3인접 행렬 구현하기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    matrixPath = [[0 for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        U, V, C = map(int, input().split())

        matrixPath[U][V] = C


    for listPath in matrixPath:
        print(*listPath)
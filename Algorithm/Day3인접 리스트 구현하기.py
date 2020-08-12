import sys
sys.stdin = open("./Algorithm/Day3인접 리스트 구현하기.txt", "r")

import bisect

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    listPath = [[] for _ in range(N)]

    for _ in range(M):
        U, V = map(int, input().split())

        bisect.insort(listPath[U], V)
        bisect.insort(listPath[V], U)

    for path in listPath:
        print(*path)
import sys
sys.stdin = open("./Algorithm/HW암기대회.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    matBoard = [[int(n) for n in input().split()] for _ in range(N)]

    

    print(matBoard)
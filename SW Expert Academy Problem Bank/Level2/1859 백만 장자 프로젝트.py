import sys

sys.stdin = open("SW Expert Academy Problem Bank/Level2/1859 백만 장자 프로젝트.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    Ns = [int(c) for c in input().split()]
    Ns.reverse()

    localMax = 0
    totalProfit = 0
    for n in Ns:
        if n > localMax:
            localMax = n
        elif n < localMax:
            totalProfit += localMax - n

    print(f'#{test_case} {totalProfit}')
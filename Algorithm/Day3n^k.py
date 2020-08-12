import sys
sys.stdin = open("./Algorithm/Day3n^k.txt", "r")

def Power(n, k, m):
    if k == 0:
        return 1
    if k == 1:
        return n

    half = Power(n, k//2, m)

    if k % 2 == 0:
        return half * half % m
    else:
        return half * half * n % m


T = int(input())
for test_case in range(1, T + 1):
    N, K, M = map(int, input().split())

    result = Power(N, K, M)
    print(result)
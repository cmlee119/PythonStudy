import sys

sys.stdin = open("SW Expert Academy Problem Bank/Level3/10200 구독자 전쟁.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())

    maxN = min(A, B)
    minN = max(-N + A + B, 0)

    print(f'#{test_case} {maxN} {minN}')
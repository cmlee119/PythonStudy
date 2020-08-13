import sys
sys.stdin = open("SW Expert Academy Problem Bank/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    total = sum([int(num) for num in input().split() if int(num[-1]) % 2 == 1])
    print(f'#{test_case} {total}')
import sys

sys.stdin = open("SW Expert Academy Problem Bank/Level3/5789 현주의 상자 바꾸기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, Q = tuple(int(i) for i in input().split())

    listResult = [0 for _ in range(N)]

    for i in range(1, Q + 1):
        L, R = tuple(int(n) for n in input().split())

        for index in range(L - 1, R):
            listResult[index] = i


    print(f"#{test_case}", end=" ")
    print(*listResult)
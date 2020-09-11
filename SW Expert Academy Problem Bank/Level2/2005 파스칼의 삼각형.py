import sys

sys.stdin = open("SW Expert Academy Problem Bank/Level2/2005 파스칼의 삼각형.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    listNum = [1 for _ in range(N)]

    print(f"#{test_case}")

    for i in range(1, N + 1):
        print(*listNum[0:i])

        for j in range(i - 1, 0, -1):
            listNum[j] = listNum[j] + listNum[j - 1]

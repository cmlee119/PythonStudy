import sys

sys.stdin = open("SW Expert Academy Problem Bank/Level2/2001 파리 퇴치.txt", "r")

def solution(N, M, NxN):
    result = 0

    for y in range(N - M + 1):
        for x in range(N - M + 1):
            score = 0
            for y_offset in range(0, M):
                for x_offset in range(0, M):
                    score += NxN[y + y_offset][x + x_offset]

            result = max(result, score)

    return result

T = int(input())
for test_case in range(1, T + 1):

    N, M = tuple(int(i) for i in input().split())
    NxN = []
    for _ in range(N):
        NxN.append(list(int(i) for i in input().split()))

    result = solution(N, M, NxN)

    print(f"#{test_case} {result}")
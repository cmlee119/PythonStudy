import sys
sys.stdin = open("./Algorithm/Day5피보나치 수열2.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    num = [1, 1]
    for i in range(N - 2):
        num[i % 2] = sum(num)

    print(max(num))
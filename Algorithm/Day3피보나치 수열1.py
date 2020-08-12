import sys
sys.stdin = open("./Algorithm/Day3피보나치 수열1.txt", "r")

listPibo = [1, 1]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    for index in range(len(listPibo), N):
        listPibo.append(listPibo[index-1] + listPibo[index-2])

    print(listPibo[N - 1])
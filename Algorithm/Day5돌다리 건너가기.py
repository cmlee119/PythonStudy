import sys
sys.stdin = open("./Algorithm/Day5돌다리 건너가기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    listStep = [0, 1, 1]

    modNum = 1904101441

    i = N
    for i in range(N - 1):
        listStep[i % 3] = ((listStep[0] % modNum + listStep[1] % modNum) % modNum + listStep[2] % modNum) % modNum

    print(listStep[i % 3])
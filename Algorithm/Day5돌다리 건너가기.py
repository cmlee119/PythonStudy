import sys
sys.stdin = open("./Algorithm/Day5돌다리 건너가기.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    listStep = [1, 2, 4]

    modNum = 1904101441

    for _ in range(N - 1):
        listStep = [listStep[1], listStep[2], sum(listStep) % modNum]

    print(listStep[0])
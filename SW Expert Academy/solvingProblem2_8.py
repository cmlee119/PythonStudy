import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    listNum = list(map(int, input().split()))

    bBigSmall = 1 #1이면 큰수 0이면 작은수

    for index in range(0, N):
        #print(listNum[index])

        maxminNum = listNum[index]
        maxminIndex = index

        for innerIndex in range(index, N):
            if bBigSmall == 1 and listNum[innerIndex] > maxminNum:
                maxminNum = listNum[innerIndex]
                maxminIndex = innerIndex
            elif bBigSmall == 0 and listNum[innerIndex] < maxminNum:
                maxminNum = listNum[innerIndex]
                maxminIndex = innerIndex

        listNum[index], listNum[maxminIndex] = listNum[maxminIndex], listNum[index]

        if bBigSmall == 1:
            bBigSmall = 0
        else:
            bBigSmall = 1

    print(f"#{test_case}", end='')
    for i in range(0,10):
        print(f" {listNum[i]}", end='')

    print()
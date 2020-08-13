import sys

sys.stdin = open("input.txt", "r")

import copy

def MyFunc(matBoard, N, listCheck, memoization):
    if len(matBoard) == 1:
        idxTarget = listCheck.index(0)
        return matBoard[0][idxTarget]

    minValue = 99999999

    for idx in range(0, N):
        item = listCheck[idx]
        if item == 0:
            memo = memoization[0].get(tuple(listCheck))
            if memo != None:
                minValue = memo
                break

            newListCheck = copy.copy(listCheck)
            newListCheck[idx] = 1

            result = MyFunc(matBoard[1:], N, newListCheck, memoization)
            result += matBoard[0][idx]

            if result < minValue:
                minValue = result

    memoization[0].update({tuple(listCheck) : minValue})

    return minValue


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    matBoard = []
    for i in range(N):
        matBoard.append(list(map(int, input().split())))

    listCheck = [0 for i in range(N)]

    memoization = [{} for i in range(N)]

    result = MyFunc(matBoard, N, listCheck, memoization)

    print(f"#{test_case} {result}")
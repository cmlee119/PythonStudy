import sys
sys.stdin = open("./Algorithm/Day4최대 합 부분 연속 수열.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    listNum = [int(strN) for strN in input().split()]

    maxValue = listNum[0]
    accumulateValue = 0
    for num in listNum:
        accumulateValue += num
        if accumulateValue > maxValue:
            maxValue = accumulateValue
        if accumulateValue < 0:
            accumulateValue = 0

    print(maxValue)



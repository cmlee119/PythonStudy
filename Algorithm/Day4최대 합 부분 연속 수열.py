import sys
sys.stdin = open("./Algorithm/Day4최대 합 부분 연속 수열.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    listNum = [int(n) for n in input().split()]

    maxValue = listNum[0]
    accumulateValue = 0
    for num in listNum:
        accumulateValue += num
        maxValue = max(maxValue, accumulateValue)
        accumulateValue = max(0, accumulateValue)

    print(maxValue)
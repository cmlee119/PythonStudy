import sys
sys.stdin = open("./Algorithm/Day4최대 합 부분 연속 수열.txt", "r")

def estimateMaxValue(listNum, start, end):
    total = 0
    for index in range(start, end):
        if listNum[index] > 0:
            total += listNum[index]
    return total

def myFunc(listNum):


    return 0

T = int(input())
for test_case in range(1, T + 1):
    listnum = [int(strN) for strN in input().split()]

    print(myFunc(listNum))


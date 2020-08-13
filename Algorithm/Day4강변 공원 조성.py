import sys
sys.stdin = open("./Algorithm/Day4강변 공원 조성.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    listNum = [int(n) for n in input().split()]

    maxArea = 0
    dictCandidate = dict()
    for index, num in enumerate(listNum):
        if num not in dictCandidate:
            dictCandidate[num] = index

        for numCandidate, indexCandidate in dictCandidate.items():
            if num < numCandidate:
                dictCandidate.pop(numCandidate)

            area = numCandidate * (index - indexCandidate + 1)
            if area > maxArea:
                maxArea = area

    print(maxArea)
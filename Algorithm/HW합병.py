import sys
sys.stdin = open("./Algorithm/HW합병.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    listN = [int(n) for n in input().split()]
    listM = [int(n) for n in input().split()]

    listResult = [0 for _ in range(len(listN) + len(listM))]

    indexN = 0
    indexM = 0
    indexResult = 0
    while indexN < len(listN) and indexM < len(listM):
        if listN[indexN] < listM[indexM]:
            listResult[indexResult] = 1
            indexN += 1
        else:
            listResult[indexResult] = 2
            indexM += 1
        
        indexResult += 1

    for _ in range(indexN, len(listN)):
        listResult[indexResult] = 1
        indexResult += 1

    for _ in range(indexM, len(listM)):
        listResult[indexResult] = 2
        indexResult += 1

    print(*listResult)
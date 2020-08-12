import sys
sys.stdin = open("./Algorithm/Day3이진탐색.txt", "r")

def binary_search(listNum, T, lo = 0, hi = None):
    if hi == None:
        hi = len(listNum) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2

        if T < listNum[mid]:
            hi = mid - 1
        elif T > listNum[mid]:
            lo = mid + 1
        elif T == listNum[mid]:
            return mid

    return -1 

T = int(input())
for test_case in range(1, T + 1):
    listN = [int(c) for c in input().split()]
    listM = [int(c) for c in input().split()]

    listResult = [binary_search(listN, m) for m in listM]
    
    print(*listResult)
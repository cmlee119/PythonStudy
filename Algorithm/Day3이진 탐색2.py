import sys
sys.stdin = open("./Algorithm/Day3이진 탐색2.txt", "r")

def binarySearchCustom(listNum, T, lo = 0, hi = None):
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

    right = min(len(listNum) - 1, lo)
    left = max(0, hi)

    if T - listNum[left] <= listNum[right] - T:
        return left
    else:
        return right

T = int(input())
for test_case in range(1, T + 1):
    listN = [int(i) for i in input().split()]
    listM = [int(i) for i in input().split()]

    listResult = [listN[binarySearchCustom(listN, m)] for m in listM]
    
    print(*listResult)

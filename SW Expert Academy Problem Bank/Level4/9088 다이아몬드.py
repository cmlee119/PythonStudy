import sys

sys.stdin = open("SW Expert Academy Problem Bank/Level4/9088 다이아몬드.txt", "r")

def customBisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid][0] < x: lo = mid+1
        else: hi = mid
    return lo

T = int(input())
for test_case in range(1, T + 1):
    N, K = tuple(int(strNum) for strNum in input().split())
    listNum = [int(input()) for _ in range(N)]

    listDiamondCount = [[num, 0] for num in sorted(set(listNum))]

    maxValue = 0
    for num in listNum:
        index = customBisect(listDiamondCount, num)
        for leftAddIndex in range(0, K + 1):
            leftIndex = index - leftAddIndex
            if leftIndex < 0:
                break
            if num - listDiamondCount[leftIndex][0] > K:
                continue

            listDiamondCount[leftIndex][1] += 1
            if listDiamondCount[leftIndex][1] > maxValue:
                maxValue = listDiamondCount[leftIndex][1]

    print(f'#{test_case} {maxValue}')
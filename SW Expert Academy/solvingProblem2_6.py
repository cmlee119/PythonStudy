import sys
import copy

sys.stdin = open("input.txt", "r")

setNum = set()

NUM_MAX = 12

def func(numList):
    #조건에 맞는 순열인지 검사
    if numList[N-1] <= NUM_MAX and sum(numList) == K:
        num = 0
        for i in range(0, len(numList)):
            num += numList[i]
            num *= 100

        setNum.add(num)
        print(num)
    else:
        numList[N-1] += 1
    
    #순열 숫자간의 차이를 줄이고 재귀호출
    for i in range(1, len(numList)):
        if numList[i] - numList[i-1] > 2:
            numList[i] -= 1
            numList[i-1] += 1
            
            func(copy.copy(numList))

T = int(input())
for test_case in range(1, T + 1):
    setNum.clear()
    N, K = map(int, input().split())

    numList = [i + 1 for i in range(N)]
    numList[N-1] += K - sum(numList)
    i = 0
    for index in range(N-1, 0, -1):
        localNumMax = NUM_MAX - i
        if numList[index] > localNumMax:
            numList[index-1] += numList[index] - localNumMax
            numList[index] = localNumMax

        i += 1

    func(numList)

    print(f"#{test_case} {len(setNum)}")
        



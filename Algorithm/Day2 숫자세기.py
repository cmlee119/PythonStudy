import sys
sys.stdin = open("./Algorithm/Day2 숫자세기.txt", "r")


T = int(input())

for _ in range(T):
    listNum = list(int(n) for n in input().split())
    listFindNum = list(int(n) for n in input().split())

    dictFindNum = dict()
    for m in listFindNum:
        if m in dictFindNum:
            pass
        else:
            dictFindNum[m] = 0

    for n in listNum:
        if n in dictFindNum:
            dictFindNum[n] += 1
        
    listResult = [dictFindNum[m] for m in listFindNum]
        
    print(*listResult)
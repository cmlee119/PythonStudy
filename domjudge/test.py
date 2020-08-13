import heapq

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
   
    listNum = list(map(int, input().split()))

    listMulNum = [1]

    hq = []
    for i, num in enumerate(listNum):
        heapq.heappush(hq, (num, (i, 0)))

    while len(listMulNum) < N:
        minValue, tupleData = heapq.heappop(hq)
        indexOfListNum, indexOfListMulNum = tupleData

        if minValue != listMulNum[-1]:
            listMulNum.append(minValue)

        indexOfListMulNum += 1
        newValue = listNum[indexOfListNum] * listMulNum[indexOfListMulNum]
        
        heapq.heappush(hq, (newValue, (indexOfListNum, indexOfListMulNum)))

    print(listMulNum[N-1])
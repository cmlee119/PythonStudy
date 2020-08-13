import sys
sys.stdin = open("./Algorithm/HW최단 경로 구하기.txt", "r")

import heapq

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    listEdge = [[] for _ in range(N)]

    for _ in range(M):
        U, V, C = map(int, input().split())
        listEdge[U].append((V, C))

    listCheck = [None for _ in range(N)]
    listCheck[0] = 0
    hq = []
    heapq.heappush(hq, (0, 0))

    result = -1

    while len(hq) > 0:
        currentNode, currentCost = heapq.heappop(hq)

        for nextNode, nextCost in listEdge[currentNode]:
            cost = currentCost + nextCost

            if listCheck[nextNode] != None and cost >= listCheck[nextNode]:
                continue

            listCheck[nextNode] = cost

            if nextNode == N - 1:
                result = cost
                break

            heapq.heappush(hq, (nextNode, cost))

    print(result)
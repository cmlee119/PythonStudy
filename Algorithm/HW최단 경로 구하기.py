import sys
sys.stdin = open("./Algorithm/HW최단 경로 구하기.txt", "r")

import heapq

T = int(input())
for test_case in range(1, T + 1):
    N, M = (int(n) for n in input().split())

    listEdge = [[] for _ in range(N)]
    for _ in range(M):
        U, V, C = (int(n) for n in input().split())
        listEdge[U].append((V, C))

    visited = [False for _ in range(N)]
    hq = []
    heapq.heappush(hq, (0, 0))

    endNode = N - 1

    result = -1

    while len(hq) > 0:
        currentCost, currentNode = heapq.heappop(hq)
        
        visited[currentNode] = True

        if currentNode == endNode:
            result = currentCost
            break

        for node, cost in listEdge[currentNode]:
            nextCost = currentCost + cost

            if visited[node] == True:
                continue

            heapq.heappush(hq, (nextCost, node))

    print(result)
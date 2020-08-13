import sys
sys.stdin = open("./Algorithm/Day4최소신장트리MST.txt", "r")

import heapq

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    listEdge = [[] for _ in range(N)]

    for _ in range(M):
        U, V, C = map(int, input().split())
        listEdge[U].append((V, C))
        listEdge[V].append((U, C))

    listNode = []

    listCheck = set()
    hq = []
    heapq.heappush(hq, (0, 0))
    for _ in range(N):
        currentCost, currentNode = heapq.heappop(hq)
        listCheck.add(currentNode)
        listNode.append(currentCost)

        for nextNode, nextCost in listEdge[currentNode]:
            if nextNode in listCheck:
                continue
            
            heapq.heappush(hq, (nextCost, nextNode))

    print(sum(listNode))

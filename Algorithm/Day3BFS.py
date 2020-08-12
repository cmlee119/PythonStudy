import sys
sys.stdin = open("./Algorithm/Day3BFS.txt", "r")

import bisect
import collections as std

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    listPath = [[] for _ in range(N)]

    for _ in range(M):
        U, V = map(int, input().split())

        bisect.insort(listPath[U], V)

    setCheck = set()
    queue = std.deque([])
    queue.append(0)
    setCheck.add(0)

    while len(queue) > 0:
        node = queue.popleft()
        print(node, end = ' ')

        for nextNode in listPath[node]:
            if nextNode not in setCheck:
                queue.append(nextNode)
                setCheck.add(nextNode)
    print()
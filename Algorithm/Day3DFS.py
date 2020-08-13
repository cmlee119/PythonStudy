import sys
sys.stdin = open("./Algorithm/Day3DFS.txt", "r")

import bisect

def DFS(listPath, currentNode, setCheck = set()):
    print(currentNode, end=' ')
    setCheck.add(currentNode)
    for nextNode in listPath[currentNode]:
        if nextNode not in setCheck:
            DFS(listPath, nextNode, setCheck)

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    listPath = [[] for _ in range(N)]

    for _ in range(M):
        U, V = map(int, input().split())

        bisect.insort(listPath[U], V)
        bisect.insort(listPath[V], U)

    DFS(listPath, 0)
    print()
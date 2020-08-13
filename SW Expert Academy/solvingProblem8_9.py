import sys

sys.stdin = open("SW Expert Academy/solvingProblem8_9.txt", "r")

def MyFunc(N, indexNode, listNode):
    if indexNode * 2 < N:
        listNode[indexNode] = MyFunc(N, indexNode * 2, listNode) + MyFunc(N, indexNode * 2 + 1, listNode)
    elif indexNode * 2 == N:
        listNode[indexNode] = MyFunc(N, indexNode * 2, listNode)
    return listNode[indexNode]
    
T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())

    listNode = [None for _ in range(N+1)]

    for _ in range(M):
        I, V = map(int, input().split())
        listNode[I] = V

    MyFunc(N, 1, listNode)

    print(f"#{test_case} {listNode[L]}")
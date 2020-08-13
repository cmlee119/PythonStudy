import sys

sys.stdin = open("SW Expert Academy/solvingProblem8_7.txt", "r")

def MyFunc(N, indexNode, value, listNode):
    if indexNode > N:
        return value

    listNode[indexNode] = MyFunc(N, indexNode * 2, value, listNode) + 1

    return MyFunc(N, indexNode * 2 + 1, listNode[indexNode], listNode)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    listNode = [0 for _ in range(N+1)]

    MyFunc(N, 1, 0, listNode)

    print(f"#{test_case} {listNode[1]} {listNode[N//2]}")
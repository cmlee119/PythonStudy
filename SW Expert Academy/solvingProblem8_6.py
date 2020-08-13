import sys

sys.stdin = open("SW Expert Academy/solvingProblem8_6.txt", "r")

def MyFunc(N, listNode):
    if N == 0:
        return 0

    return MyFunc(listNode[N][0], listNode) + MyFunc(listNode[N][1], listNode) + 1

T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())

    inputData = list(map(int, input().split()))

    iMax = max(inputData)

    listNode = [[0, 0] for _ in range(iMax + 1)]

    for i in range(E):
        P = inputData[i * 2]
        C = inputData[i * 2 + 1]

        if listNode[P][0] == 0:
            listNode[P][0] = C
        else:
            listNode[P][1] = C

    result = MyFunc(N, listNode)

    print(f"#{test_case} {result}")
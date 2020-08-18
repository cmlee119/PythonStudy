import sys
sys.stdin = open("./Algorithm/HW무거운 용액.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, C = tuple(int(n) for n in input().split())

    listGramVolume = [[int(E) for E in input().split()] for _ in range(N)]
    listGramVolume.sort(key=lambda t:t[0]/t[1], reverse=True)

    V = C
    resultMass = 0
    for gramVolume in listGramVolume:
        if gramVolume[1] > V:
            subVolume = V
            resultMass += subVolume * gramVolume[0] / gramVolume[1]
        else:
            subVolume = gramVolume[1]
            resultMass += gramVolume[0]

        V -= subVolume
        if V == 0:
            break

    print(int(resultMass))
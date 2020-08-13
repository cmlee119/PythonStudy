import sys
sys.stdin = open("./Algorithm/HW무거운 용액.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, C = map(int, input().split())

    listGramVolume = [[int(E) for E in input().split()] for _ in range(N)]
    listGramVolume.sort(key=lambda t:t[0]/t[1], reverse=True)

    V = C
    resultMass = 0
    for gramVolume in listGramVolume:
        subVolume = min(V, gramVolume[1])
        resultMass += subVolume * gramVolume[0] / gramVolume[1]
        V -= subVolume
        if V == 0:
            break

    print(int(resultMass))
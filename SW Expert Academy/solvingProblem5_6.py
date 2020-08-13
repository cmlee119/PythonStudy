import sys

sys.stdin = open("input.txt", "r")

def Game(Player, LeftIndex, RightIndex):
    L = Player[LeftIndex]
    R = Player[RightIndex]

    if L == 1 and R == 3:
        return -1
    if L == 3 and R == 1:
        return 1
    if L < R:
        return 1
    if L > R:
        return -1
    return -1

def GetWinner(N, player, i, j):
    if i == j:
        return i

    idxLeftWinner = GetWinner(N, player, i, (i+j)//2)
    idxRightWinner = GetWinner(N, player, (i+j)//2+1, j)

    result = Game(player, idxLeftWinner, idxRightWinner)
    if result == -1:
        return idxLeftWinner
    else:
        return idxRightWinner 


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    player = list(map(int, input().split()))

    result = GetWinner(N, player, 0, N - 1) + 1

    print(f"#{test_case} {result}")


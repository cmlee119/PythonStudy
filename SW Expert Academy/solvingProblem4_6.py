import sys

sys.stdin = open("input.txt", "r")

listBoard = [0,1,3,5]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) // 10

    #계산하기 쉽게 그냥 10 나누기
    #길이 생각하기 쉽게 0 버리고 1부터 시작
    if N >= len(listBoard):
        for i in range(len(listBoard),N+1):
            listBoard.append(listBoard[i-1] + listBoard[i-2] * 2)

    print(f"#{test_case} {listBoard[N]}")


    
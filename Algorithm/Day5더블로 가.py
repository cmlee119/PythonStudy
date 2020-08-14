import sys
sys.stdin = open("./Algorithm/Day5더블로 가.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    listNum = [0]
    listNum += [int(n) for n in input().split()]

    listMaxScore = listNum[:2]

    for index in range(2, N + 1):
        if index % 2 == 0:
            score = listNum[index] + max(listMaxScore[index // 2] ,listMaxScore[index - 1], listMaxScore[index - 2])
        else:
            score = listNum[index] + max(listMaxScore[index - 1], listMaxScore[index - 2])

        listMaxScore.append(score)

    print(listMaxScore[-1])




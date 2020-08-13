import sys
sys.stdin = open("./Algorithm/Day4행사 참가하기.txt", "r")

def isContain(x, line):
    if line[0] <= x and x <= line[1]:
        return True

    return False

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    listLine = []
    for _ in range(N):
        listLine.append(tuple(int(n) for n in input().split()))

    listLine.sort(key=lambda a:a[1])

    count = 1
    last = listLine[0][1]
    for line in listLine:
        if isContain(last, line) == True:
            pass
        else:
            last = line[1]
            count += 1

    print(count)

        



    
import sys

sys.stdin = open("SW Expert Academy Problem Bank/Level3/1225 암호생성기.txt", "r")

for _ in range(10):
    T = input()

    listNum = [int(i) for i in input().split()]

    count = 1
    while True:
        num = listNum.pop(0) - count
        count += 1
        if count > 5:
            count = 1

        if num <= 0:
            listNum.append(0)
            break

        listNum.append(num)

    print(f'#{T}', *listNum)
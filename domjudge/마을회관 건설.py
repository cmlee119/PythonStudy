T = int(input())

def myFunc(x):
    total = 0
    for num in listNum:
        total += abs(num - x)
    return total

for _ in range(T):
    listNum = list(map(int, input().split()))

    print(myFunc(listNum[len(listNum)//2]))
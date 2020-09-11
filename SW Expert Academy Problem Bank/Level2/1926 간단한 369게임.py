import sys

sys.stdin = open("SW Expert Academy Problem Bank/Level2/1926 간단한 369게임.txt", "r")

N = int(input())

for i in range(1, N + 1):
    strNum = str(i)

    count = 0
    for char in strNum:
        if char in ['3', '6', '9']:
            count += 1
            
    result = '-' * count if count > 0 else strNum

    print(result, end=' ')
    
print()
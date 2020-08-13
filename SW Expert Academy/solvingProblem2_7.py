import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    bookPageNum, tA, tB = map(int, input().split())

    #A사람
    lA = lB = 1
    rA = rB = bookPageNum

    findA = False
    findB = False
    while findA == False and findB == False:
        cA = int((lA + rA)//2)
        if tA == cA:
            findA = True
        elif tA < cA:
            rA = cA
        else:# tA > cA
            lA = cA

        cB = int((lB + rB)//2)
        if tB == cB:
            findB = True
        elif tB < cB:
            rB = cB
        else:# tA > cA
            lB = cB

    result = ""
    if findA == True and findB == True:
        result = "0"
    elif findA == True:
        result = "A"
    elif findB == True:
        result = "B"

    print(f"#{test_case} {result}")
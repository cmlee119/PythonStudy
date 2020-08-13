import sys

sys.stdin = open("input.txt", "r")

stackList = []
def StackPush(item):
    stackList.append(item)

def StackPop():
    if len(stackList) <= 0:
        return None
    return stackList.pop()

def StackClear():
    stackList.clear()

def StackTop():
    if StackLen() == 0:
        return None
    return stackList[StackLen() - 1]

def StackLen():
    return len(stackList)

T = int(input())
for test_case in range(1, T + 1):
    StackClear()
    
    S = str(input())

    for char in S:
        #스택 Top 글자와 같으면 Pop
        if char == StackTop():
            StackPop()
        #아니면 글자를 Push
        else:
            StackPush(char)

    print(f"#{test_case} {StackLen()}")
import sys

sys.stdin = open("input.txt", "r")

stackList = []

def StackPush(char):
    stackList.append(char)

def StackPop():
    if len(stackList) <= 0:
        return None
    
    return stackList.pop()

def StackClear():
    stackList.clear()

def MyFunc(strInput):
    StackClear()
    
    for char in strInput:
        if char in ['{', '(']:
            StackPush(char)
        elif char == '}':
            if StackPop() != '{':
                return 0
        elif char == ')':
            if StackPop() != '(':
                return 0

    if StackPop() != None:
        return 0
    
    return 1

T = int(input())
for test_case in range(1, T + 1):
    strInput = str(input())

    print(f"#{test_case} {MyFunc(strInput)}")

    



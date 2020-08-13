import sys

sys.stdin = open("input.txt", "r")

class Stack:
    stackList = []
    def Push(self, item):
        self.stackList.append(item)

    def Pop(self):
        if len(self.stackList) <= 0:
            return None
        return self.stackList.pop()

    def Clear(self):
        self.stackList.clear()

    def Len(self):
        return len(self.stackList)

def MyFunc(strCommand):
    stack = Stack()
    stack.Clear()
    try:
        for char in strCommand:
            if char == '+':
                stack.Push(stack.Pop() + stack.Pop())
            elif char == '-':
                A, B = stack.Pop(), stack.Pop()
                stack.Push(B - A)
            elif char == '*':
                stack.Push(stack.Pop() * stack.Pop())
            elif char == '/':
                A, B = stack.Pop(), stack.Pop()
                stack.Push(B // A)
            elif char == '.':
                if stack.Len() != 1:
                    break
                return stack.Pop()
            else:
                stack.Push(int(char))
    except:
        return "error"
    
    return "error"

T = int(input())
for test_case in range(1, T + 1):
    strCommand = list(map(str, input().split()))

    result = MyFunc(strCommand)

    print(f"#{test_case} {result}")

    



    


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

def IsCorrectPosition(T, N):
    if T[0] < 0 or T[0] >= N or T[1] < 0 or T[1] >= N:
        return False
    return True

def FindPath(N, C, M):
    D4 = ((1,0),(-1,0),(0,-1),(0,1))

    for D in D4:
        T = tuple(sum(e) for e in zip(C, D))
        if IsCorrectPosition(T, N) == True and M[T[0]][T[1]] in (0, 3):
            return T

    return None

def MyFunc(N, M, S, E):
    stack = Stack()
    stack.Clear()

    Current = S
    Next = None

    while True:
        #현재 위치 C 에서 벽을 제외하고 갈 수 있는곳 N 을 찾는다.
        #만약 찾지 못한다면 이전 경로로 돌아간다 즉 스택에서 하나 꺼내서 C에 넣고 처음부터 다시 반복한다.
        #N이 이미 가본곳인지 체크한다.(가본곳은 벽으로 바뀌므로 위에서 미리 검사가 된다. 이건 필요 없다.)
        Next = FindPath(N, Current, M)

        if Next != None:
            #N이 종료 지점인지 검사한다.
            if Next == E:
                return 1

            stack.Push(Current)
            Current = Next
            M[Current[0]][Current[1]] = 1
        else:
            if stack.Len() == 0:
                return 0

            Current = stack.Pop()
        
        
        #현재 위치 C 를 스택에 넣고 다음 칸 N을 C에 대입한다.
        #현재 위치를 가본곳으로 체크한다. 가본곳 체크는 현재 위치 C를 벽 1로 바꾸면 된다.
        #반복한다.

    return 0



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    M = []
    for i in range(N):
        L = list(map(int, input()))
        for j in range(N):
            if L[j] == 2:
                S = (i, j)
            elif L[j] == 3:
                E = (i, j)

        M.append(L)

    result = MyFunc(N, M, S, E)

    print(f"#{test_case} {result}")    
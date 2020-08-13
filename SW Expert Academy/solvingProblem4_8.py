import sys

sys.stdin = open("input.txt", "r")

stackList = []
def StackPush(int):
    stackList.append(int)

def StackPop():
    if len(stackList) <= 0:
        return None
    return stackList.pop()

def StackClear():
    stackList.clear()

T = int(input())
for test_case in range(1, T + 1):
    StackClear()

    V, E = map(int, input().split())

    #node셋팅
    nodePath = [[] for i in range(V + 1)]

    #Path셋팅
    for i in range(E):
        S, E = map(int, input().split())
        nodePath[S].append(E)

    S, G = map(int, input().split())

    #가본곳 체크
    nodeCheck = [0 for i in range(V + 1)]

    #스택에는 이전에 있던곳 저장하자
    #S는 현재 위치 N은 갈곳
    while S != None:
        #S를 가본장소로 체크
        nodeCheck[S] = 1
        #S에서 갈수 있는곳 중에 안가본곳 찾아서 N에 대입
        N = 0
        for i in nodePath[S]:
            if nodeCheck[i] == 0:
                N = i
                break
        
        if N != 0:
            StackPush(S)
            S = N
        else:
            S = StackPop()

        #N이 0이 아니라면
        #   Stack에 S를 저장하고 S = N
        #N이 0이라면 Pop해서 S에 대입
        #바뀐 S로 다시 처음부터 반복
        #S가 0이라면 종료

    print(f"#{test_case} {nodeCheck[G]}")

import sys

sys.stdin = open("SW Expert Academy/input.txt", "r")

class Queue:
    listData = None
    front = 0
    Rear = 0

    def __init__(self, size):
        self.listData = [0 for _ in range(size)]
        self.front = 0
        self.Rear = 0

    def Put(self, item):
        if self.IsFull() == True:
            return False

        self.Rear = self._GetNextIndex_(self.Rear)
        self.listData[self.Rear] = item

        return True

    def Get(self):
        if self.IsEmpty() == True:
            return None

        self.front = self._GetNextIndex_(self.front)
        return self.listData[self.front]

    def IsFull(self):
        if self.front == self._GetNextIndex_(self.Rear):
            return True
        return False

    def IsEmpty(self):
        return self.front == self.Rear

    def _GetNextIndex_(self, index):
        return (index + 1) % len(self.listData)

def IsCorrectPosition(T, N):
    if T[0] < 0 or T[0] >= N or T[1] < 0 or T[1] >= N:
        return False
    return True

def FindPath(N, C, M):
    D4 = ((0,1),(0,-1),(1,0),(-1,0))

    for D in D4:
        T = tuple(sum(e) for e in zip(C, D))
        if IsCorrectPosition(T, N) == True and M[T[0]][T[1]] in (0, 3):
            return T

    return None

def MyFunc(N, M, S):
    queue = Queue(100)

    Current = S
    Next = None

    distance = 0

    while True:
        #현재 위치 C 에서 벽을 제외하고 갈 수 있는곳 N 을 찾는다.
        #만약 찾지 못한다면 이전 경로로 돌아간다 즉 스택에서 하나 꺼내서 C에 넣고 처음부터 다시 반복한다.
        #N이 이미 가본곳인지 체크한다.(가본곳은 벽으로 바뀌므로 위에서 미리 검사가 된다. 이건 필요 없다.)
        Next = FindPath(N, Current, M)

        if Next != None:
            #N이 종료 지점인지 검사한다.
            if M[Next[0]][Next[1]] == 3:
                return distance

            queue.Put((Next, distance))
            M[Next[0]][Next[1]] = 1
            
        else:
            if queue.IsEmpty():
                return 0

            Current, distance = queue.Get()
            distance += 1           
        
        
        #현재 위치 C 를 스택에 넣고 다음 칸 N을 C에 대입한다.
        #현재 위치를 가본곳으로 체크한다. 가본곳 체크는 현재 위치 C를 벽 1로 바꾸면 된다.
        #반복한다.

    return 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    matBoard = []

    for j in range(0, N):
        listNum = list(map(int, input()))

        for i in range(0, N):
            if listNum[i] == 2:
                S = (j, i)

        matBoard.append(listNum)

    result = MyFunc(N, matBoard, S)

    print(f"#{test_case} {result}")
    
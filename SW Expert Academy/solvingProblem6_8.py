import sys

sys.stdin = open("input.txt", "r")

class Queue:
    listData = None
    front = 0
    Rear = 0

    def __init__(self, size):
        self.listData = [0 for _ in range(size + 1)]
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

def MyFunc(S, Path, Check):
    Current = S

    queue = Queue(100)

    #현재 위치가 목표위치가 아니라면 계속 반복한다
    while Current != G:
        #현재 위치에서 갈 수 있는곳들을 모두 찾는다.
        for Candidate in mapPath[Current]:
            #이미 가본곳인지 검사한다.
            if listCheckNode[Candidate] == 0:
                #가본적이 없는 곳이라면 queue에 넣는다.
                #큐에 넣었으므로 이미 간곳으로 체크한다. 이때 경로 길이를 넣는다.

                listCheckNode[Candidate] = listCheckNode[Current] + 1
                queue.Put(Candidate)

        #가야할 곳 순서인 queue 에서 하나 꺼내서 현재 위치로 삼는다.
        Current = queue.Get()
        #다음 갈곳이 없다면 G는 갈 수 없는 곳이다.
        if Current == None:
            return 0

        #다시 위로 가서 반복한다.

    return listCheckNode[Current]


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    mapPath = [[] for _ in range(V)]
    mapPath.insert(0, 0)

    for _ in range(E):
        idxNodeLeft, idxNodeRight = map(int, input().split())
        mapPath[idxNodeLeft].append(idxNodeRight)
        mapPath[idxNodeRight].append(idxNodeLeft)

    S, G = map(int, input().split())

    listCheckNode = [0 for _ in range(0, V + 1)]

    result = MyFunc(S, mapPath, listCheckNode)

    print(f"#{test_case} {result}")

    


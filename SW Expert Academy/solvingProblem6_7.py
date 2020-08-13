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

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    listPizzaCi = list(map(int, input().split()))
    listPizzaCi.insert(0, 0)

    queue = Queue(N)

    for idx in range(1, N + 1):
        queue.Put((idx, listPizzaCi[idx]))

    while queue.IsEmpty() == False:
        idPizza, C = queue.Get()

        C //= 2

        if C != 0:
            queue.Put((idPizza, C))

        if queue.IsFull() == False:
            if idx < M:
                idx += 1

                queue.Put((idx, listPizzaCi[idx]))

    print(f"#{test_case} {idPizza}")

            








        

    
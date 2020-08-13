import sys

sys.stdin = open("SW Expert Academy/solvingProblem8_8.txt", "r")

class Heap:
    m_listNode = []
    m_iCount = 0

    def __init__(self, N):
        self.m_listNode = [None for _ in range(N + 1)]
        self.m_iCount = 0

    def isFull(self):
        if self.m_iCount == len(self.m_listNode) - 1:
            return True

        return False
        
    def Push(self, value):
        if self.isFull() == True:
            self.m_listNode = self.m_listNode + [None for _ in range(len(self.m_listNode))]

        insertIndex = self.m_iCount + 1

        self.m_listNode[insertIndex] = value

        while True:
            parentIndex = insertIndex // 2
            if parentIndex == 0:
                break

            if self.m_listNode[insertIndex] < self.m_listNode[parentIndex]:
                self.m_listNode[parentIndex], self.m_listNode[insertIndex] = self.m_listNode[insertIndex], self.m_listNode[parentIndex]

            insertIndex = parentIndex

        self.m_iCount += 1

    def GetCount(self):
        return self.m_iCount

    def GetAncestorsNode(self, index):
        result = []

        while True:
            parentIndex = index // 2
            if parentIndex == 0:
                break

            result.append(self.m_listNode[parentIndex])

            index = parentIndex
        
        return result

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    listNum = list(map(int, input().split()))

    heap = Heap(N)

    for v in listNum:
        heap.Push(v)

    
    result = sum(heap.GetAncestorsNode(heap.GetCount()))

    print(f"#{test_case} {result}")

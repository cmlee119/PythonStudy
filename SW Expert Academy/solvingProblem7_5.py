import sys

sys.stdin = open("SW Expert Academy/solvingProblem7_5.txt", "r")

class Node:
    value = None
    nextNode = None

    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    head = None
    rear = None
    length = 0

    def __init__(self):
        self.head = None
        self.rear = None
        self.length = 0

    def len(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def append(self, item):
        if self.isEmpty() == True:
            self.head = self.rear = Node(item, None)
        else:
            self.rear.nextNode = Node(item, None)
            self.rear = self.rear.nextNode
        self.length += 1

    def atNode(self, index):
        if index >= self.length or index < 0:
            return None

        current = self.head
        indexCurrent = 0
        while True:
            if index == indexCurrent:
                return current
            
            current = current.nextNode
            indexCurrent += 1

    def at(self, index):
        return self.atNode(index).value

    def insert(self, index, item):
        currentNode = self.atNode(index)
        if currentNode == None:
            return False

        newNode = Node(item, currentNode)

        prevNode = self.atNode(index - 1)

        if prevNode == None:
            self.head = newNode
        else:
            prevNode.nextNode = newNode

        self.length += 1

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())

    listNum = list(map(int, input().split()))
    linkedListNum = LinkedList()
    for num in listNum:
        linkedListNum.append(num)

    listAddNum = []
    for _ in range(M):
        index, value = map(int, input().split())
        listAddNum.append((index, value))

    for index, value in listAddNum:
        linkedListNum.insert(index, value)

    print(f"#{test_case} {linkedListNum.at(L)}")
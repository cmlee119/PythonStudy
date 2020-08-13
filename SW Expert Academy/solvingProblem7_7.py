import sys

sys.stdin = open("SW Expert Academy/solvingProblem7_7.txt", "r")

class Node:
    value = None
    nextNode = None
    prevNode = None

    def __init__(self, value, nextNode, prevNode):
        self.value = value
        self.nextNode = nextNode
        self.prevNode = prevNode

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
            self.head = self.rear = Node(item, None, None)
        else:
            rearNode = self.rear
            self.rear.nextNode = Node(item, None, rearNode)
            self.rear = self.rear.nextNode
        self.length += 1

    def appendLinkedList(self, linkedList):
        if self.isEmpty() == True:
            self.head = self.rear = linkedList.headNode()
        else:
            self.rear.nextNode = linkedList.getHeadNode()
            linkedList.getHeadNode().prevNode = self.rear
            self.rear = linkedList.getRearNode()
        self.length += linkedList.len()

    def atNode(self, index):
        if index >= self.length or index < 0:
            return None

        if index < self.length / 2:
            current = self.head
            indexCurrent = 0
            while True:
                if index == indexCurrent:
                    return current
                
                current = current.nextNode
                indexCurrent += 1
        else:
            current = self.rear
            indexCurrent = self.len() - 1
            while True:
                if index == indexCurrent:
                    return current
                
                current = current.prevNode
                indexCurrent -= 1

    def at(self, index):
        return self.atNode(index).value

    def getHeadNode(self):
        return self.head
    
    def getHead(self):
        if self.head == None:
            return None
        else:
            return self.head.value

    def getRearNode(self):
        return self.rear
    
    def GetRear(self):
        if self.rear == None:
            return None
        else:
            return self.rear.value

    def insert(self, index, item):
        currentNode = self.atNode(index)
        if currentNode == None:
            return False

        prevNode = self.atNode(index - 1)

        newNode = Node(item, currentNode, prevNode)

        if prevNode == None:
            self.head = newNode
        else:
            prevNode.nextNode = newNode
            currentNode.prevNode = newNode

        self.length += 1

        return True

    def insertLinkedList(self, index, linkedList):
        currentNode = self.atNode(index)
        if currentNode == None:
            return False

        newNodeFront = linkedList.getHeadNode()
        newNodeRear = linkedList.getRearNode()

        prevNode = self.atNode(index - 1)

        if prevNode == None:
            self.head = newNodeFront
        else:
            prevNode.nextNode = newNodeFront
            newNodeFront.prevNode = prevNode

        newNodeRear.nextNode = currentNode
        currentNode.prevNode = newNodeRear

        self.length += linkedList.len()

        return True

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())

    listNum = list(map(int, input().split()))

    linkedList = LinkedList()

    for num in listNum:
        linkedList.append(num)

    startIndex = 0
    for _ in range(K):
        startIndex = (startIndex + M) % linkedList.len()
        prevIndex = (startIndex - 1 + linkedList.len()) % linkedList.len()

        value = linkedList.at(prevIndex) + linkedList.at(startIndex)

        if startIndex == 0:
            linkedList.append(value)
            startIndex = linkedList.len() - 1
        else:   
            linkedList.insert(startIndex, value)

    result = ""
    for index in range(0, 10):
        reverseIndex = linkedList.len() - index - 1

        if reverseIndex >= 0:
            result += " " + str(linkedList.at(reverseIndex))

    print(f"#{test_case}{result}")

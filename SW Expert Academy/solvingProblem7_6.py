import sys

sys.stdin = open("SW Expert Academy/solvingProblem7_6.txt", "r")

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
    N, M = map(int, input().split())

    listLinkedListNum = []

    for _ in range(M):
        linkedList = LinkedList()

        for value in list(map(int, input().split())):
            linkedList.append(value)

        listLinkedListNum.append(linkedList)

    mainLinkedList = listLinkedListNum[0]

    for i in range(1, M):
        subLinkedList = listLinkedListNum[i]

        #순열의 첫번쨰 숫자
        firstNum = subLinkedList.at(0)

        #mainLinkedList 에서 firstNum보다 첫번쨰로 큰 숫자 인덱스 찾기
        index = -1
        for i in range(mainLinkedList.len()):
            if mainLinkedList.at(i) > firstNum:
                index = i
                break

        #인덱스를 못찾은 경우 마지막에 그냥 붙이기
        #그 인덱스에 subLinkedList insert하기
        if index == -1:
            mainLinkedList.appendLinkedList(subLinkedList)
        else:
            mainLinkedList.insertLinkedList(index, subLinkedList)
        
    strResult = ""
    for i in range(mainLinkedList.len() - 1, mainLinkedList.len() - 11, -1):
        strResult += " " + str(mainLinkedList.at(i))

    print(f"#{test_case}{strResult}")

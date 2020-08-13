import sys

sys.stdin = open("SW Expert Academy/solvingProblem7_8.txt", "r")

class Node:
    value = None
    prevNode = None
    nextNode = None

    def __init__(self, value, prevNode, nextNode):
        self.value = value
        self.prevNode = prevNode
        self.nextNode = nextNode

class LinkedList:
    head = None
    rear = None
    length = 0

    def __init__(self):
        self.head = None
        self.rear = None
        self.length = 0

    def initWithList(self, listInput):
        self.head = None
        self.rear = None
        self.length = 0

        for item in listInput:
            self.append(item)

    def len(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def append(self, item):
        if self.isEmpty() == True:
            self.head = self.rear = Node(item, None, None)
        else:
            rearNode = self.rear
            self.rear.nextNode = Node(item, rearNode, None)
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
        targetNode = self.atNode(index)
        if targetNode == None:
            return None

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
        if index == self.length:
            self.append(item)
            return True

        currentNode = self.atNode(index)
        if currentNode == None:
            return False

        prevNode = currentNode.prevNode
        nextNode = currentNode

        newNode = Node(item, prevNode, nextNode)

        if prevNode == None:
            self.head = newNode
        else:
            prevNode.nextNode = newNode
        if nextNode == None:
            self.rear = newNode
        else:
            nextNode.prevNode = newNode

        self.length += 1

        return True

#제대로 동작 안할 가능성 매우 높음
    def insertLinkedList(self, index, linkedList):
        if index == self.length:
            self.appendLinkedList(linkedList)
            return True

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

    def removeByIndex(self, index):
        targetNode = self.atNode(index)
        if targetNode == None:
            return False

        if targetNode == self.getHeadNode():
            self.head = targetNode.nextNode
            self.prevNode = None
        elif targetNode == self.getRearNode():
            self.rear = targetNode.prevNode
            self.nextNode = None
        else:
            targetNode.prevNode.nextNode = targetNode.nextNode
            targetNode.nextNode.prevNode = targetNode.prevNode
        
        targetNode.prevNode = targetNode.nextNode = None

        self.length -= 1

        return True


def myFunc(N, M, L, linkedList, commands):
    for command in commands:
        commandType = command[0]

        if commandType == 'I':
            linkedList.insert(command[1], command[2])
        elif commandType == 'D':
            linkedList.removeByIndex(command[1])
        elif commandType == 'C':
            linkedList.atNode(command[1]).value = command[2]

    result = linkedList.at(L)
    if result == None:
        return -1
    
    return result

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())

    linkedList = LinkedList()
    linkedList.initWithList(list(map(int, input().split())))

    commands = []
    for _ in range(M):
        strCommand = list(map(str, input().split()))
        if strCommand[0] == 'D':
            commands.append((strCommand[0], int(strCommand[1])))
        else:
            commands.append((strCommand[0], int(strCommand[1]), int(strCommand[2])))

    result = myFunc(N, M, L, linkedList, commands)

    print(f"#{test_case} {result}")
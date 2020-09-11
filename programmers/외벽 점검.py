import collections as std

def solution(n, weak, dist):
    listNode = weak
    listPath = [None for _ in range(n)]

    len_weak = len(weak)
    for index, point in enumerate(weak):
        nextPoint = weak[index + 1 if index + 1 < len_weak else 0]
        nextDist = nextPoint - point
        if nextDist < 0:
            nextDist += n

        listPath[point] = (nextPoint, nextDist)

    hq = std.deque([])
    hq.append(set(listNode))

    #일꾼 가장 빠른애부터 차례대로
    for indexWorker, distWorker in enumerate(dist[::-1]):
        #같은 차례의 일꾼을 사용한 경우의 수들을 한번에 bfs처럼 돌린다.
        newhq = std.deque([])

        for _ in range(len(hq)):
            currentRemainNode = hq.popleft()

            #시작 가능한 노드들에서 시작
            for node in currentRemainNode:
                currentNode = node
                #시계방향,정방향
                #현재 일꾼이 갈 수 있는 만큼 간다
                newRemainNode = currentRemainNode.copy()

                remainDist = distWorker
                while currentNode in newRemainNode:
                    newRemainNode.remove(currentNode)
                    if len(newRemainNode) == 0:
                        return indexWorker + 1

                    nextNode, nextDist = listPath[currentNode]
                    #다음노드까지 갈 수 있는가?
                    if remainDist < nextDist:
                        break

                    remainDist -= nextDist
                    currentNode = nextNode

                isPass = False
                for setNode in newhq:
                    if newRemainNode.issuperset(setNode):
                        isPass = True
                        break

                if isPass == False:
                    newhq.append(newRemainNode)

        hq = newhq

    return -1

# n = 12
# weak = [1, 5, 6, 10]
# dist = [1, 2, 3, 4]

n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]

print(solution(n, weak, dist))
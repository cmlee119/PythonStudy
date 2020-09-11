import heapq

def solution(n, weak, dist):
    listNode = weak
    listPath = [None for _ in range(n)]

    for index, point in enumerate(weak):
        prevPoint = weak[index - 1]
        prevDist = point - prevPoint
        if prevDist < 0:
            prevDist += n

        nextPoint = weak[index + 1 if index + 1 < len(weak) else 0]
        nextDist = nextPoint - point
        if nextDist < 0:
            nextDist += n

        listPath[point] = (nextPoint, nextDist)

    hq = []
    heapq.heappush(hq, (len(weak), set()))
    #앞은 남은 weak 개수, 뒤는 방문한 노드들 set

    #일꾼 가장 빠른애부터 차례대로
    for indexWorker, distWorker in enumerate(dist[::-1]):
        #같은 차례의 일꾼을 사용한 경우의 수들을 한번에 bfs처럼 돌린다.
        newhq = []

        for _ in range(len(hq)):
            _, currentVisited = heapq.heappop(hq)

            #시작 가능한 노드들에서 시작
            for node in listNode:
                #이미 방문한 노드 제외
                if node in currentVisited:
                    continue

                currentNode = node
                newVisited = currentVisited.copy()
                #시계방향,정방향
                #현재 일꾼이 갈 수 있는 만큼 간다
                remainDist = distWorker
                while True:
                    newVisited.add(currentNode)

                    #방문한 노드의 수와 전체 노드의 수가 같다면 전부다 방문한 것이다.
                    if len(newVisited) == len(listNode):
                        return indexWorker + 1

                    nextNode, nextDist = listPath[currentNode]

                    #다음노드가 이미 방문한 노드라면 현재 일꾼은 일이 끝난다.
                    if nextNode in newVisited:
                        break

                    #다음노드까지 갈 수 있는가?
                    if remainDist < nextDist:
                        break

                    remainDist -= nextDist
                    currentNode = nextNode

                heapq.heappush(newhq, (len(listNode) - len(newVisited), newVisited))

        hq = newhq

    return -1

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

# n = 12
# weak = [1, 3, 4, 9, 10]
# dist = [3, 5, 7]

print(solution(n, weak, dist))
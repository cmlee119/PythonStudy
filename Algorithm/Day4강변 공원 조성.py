import sys
sys.stdin = open("./Algorithm/Day4강변 공원 조성.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    listNum = [int(n) for n in input().split()]
    listNum.append(0)

    listStart = []
    prevDistance = 0
    maxArea = 0
    for index, distance in enumerate(listNum):
        if distance > prevDistance:
            listStart.append((distance, index))
        elif distance < prevDistance:
            indexLast = 0

            for indexReverse in range(len(listStart) - 1, -1, -1):
                dataStart = listStart[indexReverse]

                if dataStart[0] > distance:
                    _, indexLast = listStart.pop()

                    newArea = dataStart[0] * (index - dataStart[1])
                    if newArea > maxArea:
                        maxArea = newArea
                else:
                    break
            
            if (len(listStart) == 0 or listStart[-1][0] != distance) and distance > 0:
                listStart.append((distance, indexLast))

        prevDistance = distance
                    

    print(maxArea)
def findLevelAndIndex(point):
    left = right = 1
    level = 0
    while True:
        if left <= point and point <= right:
            for i in range(level + 1):
                if point == left + i:
                    return level, i
            else: 
                return level, 0
        
        level += 1
        left += level
        right = left + level

def myFunc(a, b):
    upperPoint = min(a, b)
    lowerPoint = max(a, b)

    upperLevel, upperIndex = findLevelAndIndex(upperPoint)
    lowerLevel, lowerIndex = findLevelAndIndex(lowerPoint)

    levelDiff = lowerLevel - upperLevel

    if lowerIndex <= upperIndex:
        indexDiff = upperIndex - lowerIndex
    elif lowerIndex >= upperIndex + levelDiff:
        indexDiff = lowerIndex - (upperIndex + levelDiff)
    else:
        indexDiff = 0

    return levelDiff + indexDiff

T = int(input())
for test_case in range(1, T + 1):
    a, b = tuple(int(n) for n in input().split())

    result = myFunc(a, b)

    print(f"#{test_case} {result}")
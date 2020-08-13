import sys

sys.stdin = open("SW Expert Academy Problem Bank/Level3/5215 햄버거 다이어트.txt", "r")

def getEstimationMaxScore(listScoreCalorie, limitCalorie):
    maxScore = 0
    for score, calorie in listScoreCalorie:
        if calorie <= limitCalorie:
            maxScore += score
            limitCalorie -= calorie
        else:
            maxScore += score / calorie * limitCalorie
            break
    return maxScore

def getOptimalScore(listScoreCalorie, limitCalorie):
    maxScore = 0
    for index, tupleData in enumerate(listScoreCalorie):
        score, calorie = tupleData

        if calorie > limitCalorie:
            continue

        if score + getEstimationMaxScore(listScoreCalorie[index + 1:], limitCalorie - calorie) < maxScore:
            break

        subScore = score + getOptimalScore(listScoreCalorie[index + 1:], limitCalorie - calorie)
        if subScore > maxScore:
            maxScore = subScore

    return maxScore

T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    listScoreCalorie = [tuple(int(strNum) for strNum in input().split()) for _ in range(N)] #n
    listScoreCalorie.sort(key=lambda T: T[0] / T[1], reverse=True) #nlogn

    result = getOptimalScore(listScoreCalorie, L)
    
    print(f'#{test_case} {result}')
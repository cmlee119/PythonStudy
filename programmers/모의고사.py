def get1Student(index):
    return index % 5 + 1

def get2Student(index):
    listNum = [1,3,4,5]
    if index % 2 == 0:
        return 2
    else:
        return listNum[(index // 2) % 4]

def get3Student(index):
    listNum = [3,1,2,4,5]
    return listNum[(index // 2) % 5]


def solution(answers):
    listScoreTotal = [0 for _ in range(3)]

    for i in range(0, len(answers)):
        item = answers[i]
        if item == get1Student(i):
            listScoreTotal[0] += 1
        if item == get2Student(i):
            listScoreTotal[1] += 1
        if item == get3Student(i):
            listScoreTotal[2] += 1

    iMax = 0
    for score in listScoreTotal:
        if score >= iMax:
            iMax = score

    answer = []
    for i in range(0, len(listScoreTotal)):
        score = listScoreTotal[i]
        if score == iMax:
            answer.append(i + 1)

    return answer

#answers = [1,2,3,4,5]
answers = [1,3,2,4,2]

print(solution(answers))
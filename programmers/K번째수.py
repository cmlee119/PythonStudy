def solution(array, commands):
    answer = []

    for command in commands:
        newArray = array[command[0] - 1:command[1]]
        newArray.sort()
        answer.append(newArray[command[2] - 1])
    
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))
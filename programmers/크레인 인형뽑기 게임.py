def solution(board, moves):
    stackDoll = []
    
    answer = 0
    
    for move in moves:
        for y in range(0, len(board)):
            idDoll = board[y][move-1]
            board[y][move - 1] = 0
            if idDoll != 0:
                stackDoll.append(idDoll)

                while len(stackDoll) >= 2:
                    if stackDoll[len(stackDoll)-1] == stackDoll[len(stackDoll)-2]:
                        stackDoll.pop()
                        stackDoll.pop()
                        answer += 2
                    else:
                        break

                break
        
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))
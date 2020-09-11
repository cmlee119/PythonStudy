def is_beam(mat, x, y):
    return mat[x][y] != None and mat[x][y] >= 1

def is_pillar(mat, x, y):
    return mat[x][y] != None and mat[x][y] % 2 == 0

def add_structure(mat, x, y, a):
    if mat[x][y] == None:
        mat[x][y] = a
    elif mat[x][y] != a:
        mat[x][y] = 2

def remove_structure(mat, x, y, a):
    if mat[x][y] == a:
        mat[x][y] = None
    elif mat[x][y] == 2:
        if a == 0:
            mat[x][y] = 1
        else:
            mat[x][y] = 0

def check(n, mat, x, y):
    x_left = x - 1
    x_right = x + 1
    y_down = y - 1
    #기둥이 있을 경우 문제 여부 확인
    if is_pillar(mat, x, y) == True:
        if y == 0 or (x_left >= 0 and is_beam(mat, x_left, y) == True) or is_beam(mat, x, y) == True or (y_down >= 0 and is_pillar(mat, x, y_down) == True):
            #문제 없음
            pass
        else:
            return False
        
    if is_beam(mat, x, y) == True:
        if (y_down >= 0 and is_pillar(mat, x, y_down) == True) or (y_down >= 0 and x_right <= n and is_pillar(mat, x_right, y_down) == True) or (x_left >= 0 and is_beam(mat, x_left, y) == True and x_right <= n and is_beam(mat, x_right, y) == True):
            pass
        else:
            return False

    return True

def solution(n, build_frame):
    matrix = [[None for _ in range(n + 1)] for _ in range(n + 1)]

    for built_item in build_frame:
        x, y, a, b = tuple(built_item)

        temp = matrix[x][y]
        if b == 1:
            add_structure(matrix, x, y, a)
            if check(n, matrix, x, y) == False:
                matrix[x][y] = temp
        else:
            remove_structure(matrix, x, y, a)
            if a == 0: #지운게 기둥이라면
                if check(n, matrix, x, y + 1) == False or check(n, matrix, x - 1, y + 1) == False:
                    matrix[x][y] = temp

            if a == 1:
                if check(n, matrix, x - 1, y) == False or check(n, matrix, x, y) == False or check(n, matrix, x + 1, y) == False:
                    matrix[x][y] = temp

    answer = []

    for x in range(n + 1):
        for y in range(n + 1):
            if is_pillar(matrix, x, y) == True:
                answer.append([x, y, 0])
            if is_beam(matrix, x, y) == True:
                answer.append([x, y, 1])

    return answer

# n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(5, build_frame))
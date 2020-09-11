def checklock(key, lock, x_key_slide, y_key_slide):
    M = len(key)
    N = len(lock)

    for y_lock in range(N):
        for x_lock in range(N):
            x_key = -x_key_slide + x_lock
            y_key = -y_key_slide + y_lock
            
            if x_key < 0 or x_key >= M or y_key < 0 or y_key >= M:
                key_value = 0
            else:
                key_value = key[y_key][x_key]

            if key_value == lock[y_lock][x_lock]:
                return False

    return True

def transpose(mat):
    M = len(mat)
    newMat = [[0 for _ in range(M)] for _ in range(M)]
    for y in range(M):
        for x in range(M):
            newMat[x][M - y - 1] = mat[y][x]
    return newMat

def solution(key, lock):
    #4가지 방향 돌려가면서 체크
    M = len(key)
    N = len(lock)

    for _ in range(4):
        for y_key_slide in range(-M + 1, N):
            for x_key_slide in range(-M + 1, N):
                if True == checklock(key, lock, x_key_slide, y_key_slide):
                    return True

        key = transpose(key)

    return False

# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
key = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
lock = [[1, 1, 1], [1, 1, 1], [0, 0, 0]]

print(str(solution(key, lock)).lower())
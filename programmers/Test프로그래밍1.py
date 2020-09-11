def solution(v):
    if v[0][0] == v[1][0]:
        x = v[2][0]
    elif v[1][0] == v[2][0]:
        x = v[0][0]
    else:
        x = v[1][0]

    if v[0][1] == v[1][1]:
        y = v[2][1]
    elif v[1][1] == v[2][1]:
        y = v[0][1]
    else:
        y = v[1][1]

    return [x, y]

# v = [[1, 4], [3, 4], [3, 10]]
v = [[1, 1], [2, 2], [1, 2]]

print(solution(v))
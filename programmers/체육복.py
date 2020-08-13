def solution(n, lost, reserve):
    listStudent = [1 for _ in range(n + 1)]

    for l in lost:
        listStudent[l] -= 1
    for r in reserve:
        listStudent[r] += 1

    for i in range(1, len(listStudent) - 1):
        c = listStudent[i]
        c_n = listStudent[i+1]

        if c == 0 and c_n == 2:
            listStudent[i] = 1
            listStudent[i+1] = 1
        elif c == 2 and c_n == 0:
            listStudent[i] = 1
            listStudent[i+1] = 1

    return listStudent[1:].count(1) + listStudent[1:].count(2)
        
        

# n = 5
# lost = [2,4]
# reserve = [1,3,5]

n = 3
lost = [3]
reserve = [1]

print(solution(n, lost, reserve))
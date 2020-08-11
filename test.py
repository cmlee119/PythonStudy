import random

def selection(S, k):
    while True:
        vIndex = random.randint(0, len(S) - 1)
        V = S[vIndex]
        listS_L = []
        listV = []
        listS_R = []

        for num in S:
            if num < V:
                listS_L.append(num)
            elif num == V:
                listV.append(num)
            else:
                listS_R.append(num)
        
        if len(listS_L) + len(listS_R) + 1 >= len(S) * 3 // 4:
            break
            
    if k <= len(listS_L):
        return selection(listS_L, k)
    elif len(listS_L) < k and k <= len(listS_L) + len(listV):
        return V
    else:
        return selection(listS_R, k - (len(listS_L) + len(listV)))
    
    
T = int(input())
for _ in range(T):
    listNum = list(map(int, input().split()))
    k = int(input())

    result = selection(listNum, k)
    result2 = selection(listNum, len(listNum) - k + 1)

    print(abs(result2 - result))
    
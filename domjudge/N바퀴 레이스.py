import collections

def MyAlgorithm():
    N = int(input())
    List = list(map(int, input().split()))

    q_List = []
    for i in range(N):
        q = collections.deque([])
        q_List.append(q)

    dic = {}

    for c in List:
        if c in dic:
            if q_List[dic[c]][0] != c:
                return print("YES")

            q_List[dic[c]].popleft()
            dic[c] += 1
        else:
            dic[c] = 0

        q_List[dic[c]].append(c)

    return print("NO")
    print(q_List)

def main():
    T = int(input())

    for _ in range(T):
        MyAlgorithm()

main()
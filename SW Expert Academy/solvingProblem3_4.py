import sys


sys.stdin = open("input.txt", "r")

import math

def MyFunc(mat, N, M):
    for i in range(N):
        for index in range(N - M + 1):
            # 길이가 10인 스트링에서 8인 스트링을 검사할 때 중앙부터 시작하여 좌우로 흩어지면서 비교한다.
            # 예) 길이가 10인 스트링에서 8인 스트링을 검사할 때
            #     좌측값 3->0 우측값 4->7 => 좌측값 4->1 우측값 5->8 => 좌측값 5->2 우측값 6->9
            # 예) 길이가 10인 스트링에서 7인 스트링을 검사할 때
            #     가운데 값은 무시
            #     좌측값 2->0 우측값 4->6 => 좌측값 3->1 우측값 5->7 => 좌측값 4->2 우측값 6->8 => 좌측값 5->3 우측값 7->9
            leftStartIndex = index + M // 2 - 1
            rightStartIndex = index + math.ceil(M / 2)

            # 짝수는 8인 경우 3 2 1 0 => 4번
            # 홀수는 7인 경우 2 1 0 => 3번
            bFind = True
            for innerIndex in range(M // 2):
                #print(leftStartIndex - innerIndex, rightStartIndex + innerIndex)

                leftIndex = leftStartIndex - innerIndex
                rightIndex = rightStartIndex + innerIndex

                if mat[i][leftIndex] != mat[i][rightIndex]:
                    bFind = False
                    break
            
            if bFind == True:
                returnStr = ""
                for returnStrIndex in range(index, index + M):
                    returnStr += mat[i][returnStrIndex]
                return returnStr
    

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    NxN = []
    for i in range(N):
        NxN.append(input())

    # 길이가 N인 스트링에서 M인 스트링들을 검사할때 필요한 검사수는 N - M + 1 이다.
    # 예) 10 - 8 + 1 = 3 => 길이 10인 스트링에서 8인 패턴을 찾을때
    # 예) 10 - 7 + 1 = 4 => 길이 10인 스트링에서 7인 패턴을 찾을때
    returnString = MyFunc(NxN, N, M)
    if returnString != None:
        print(f"#{test_case} {returnString}")
        continue
    
    NxN_T = [[element for element in t] for t in zip(*NxN)]

    returnString = MyFunc(NxN_T, N, M)
    if returnString != None:
        print(f"#{test_case} {returnString}")
                
        

    
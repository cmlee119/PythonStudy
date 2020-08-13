T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    strPatten = str(input())    
    strTarget = str(input())

    listSkip = [i - 1 for i in range(len(strPatten), 0, -1)]

    startIndex = 0
    iFind = -1
    while startIndex <= len(strTarget) - len(strPatten):
        iFind = startIndex
        for i in range(len(strPatten)):
            pattenIndex = len(strPatten) - i - 1
            targetIndex = pattenIndex + startIndex

            #print(strPatten[pattenIndex], strTarget[targetIndex])
            if strPatten[pattenIndex] != strTarget[targetIndex]:
                
                iFind = -1
                skipIndex = len(strPatten) - i
                for j in range(len(strPatten)-1,-1,-1):
                    #print(strPatten[j], strTarget[targetIndex])
                    if strPatten[j] == strTarget[targetIndex]:
                        skipIndex = listSkip[j] - i + 1
                        break

                if skipIndex <= 0:
                    skipIndex = 1

                startIndex += 1

                break

        if iFind != -1:
            break

    #index = strTarget.find(strPatten)
    index = iFind

    if index == -1:
        index = 0
    else:
        index = 1

    print(f&quot;#{test_case} {index}&quot;)
def solution(participant, completion):
    participant.sort()  #nlogn
    completion.sort()   #nlogn
    completion.append("")

    for i in range(0, len(participant)):    #n
        if participant[i] != completion[i]:
            return participant[i]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))
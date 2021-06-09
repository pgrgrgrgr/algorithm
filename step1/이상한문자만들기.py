def solution(s):
    spacelist = s.split(" ")
    answer=''
    for i in spacelist:
        for j in range(0,len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += " "
    return answer[:-1]
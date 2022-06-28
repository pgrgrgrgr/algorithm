def solution(answers):
    answer = []
    sc={0:0,1:0,2:0}
    s=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    for i in range(len(answers)):
            if answers[i] == s[0][i%5]:
                sc[0]+=1
            if answers[i] == s[1][i%8]:
                sc[1]+=1
            if answers[i] == s[2][i%10]:
                sc[2]+=1
    for key,value in sc.items():
        if value == max(sc.values()):
            answer.append(key+1)
    return answer 

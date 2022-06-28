def solution(N, stages):
    answer=[]
    returnlist = []
    stages.sort() 
    failure={}
    for i in range(N):
        try:
            failure[i+1] = stages.count(i+1)/len(stages)
        except ZeroDivisionError:
            failure[i+1] = 0
        stages = stages[stages.count(i+1):]
    returnlist = sorted(failure.items(),reverse = True,key = lambda x:x[1])
    for i,j in returnlist:
        answer.append(i)
    return answer   

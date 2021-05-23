def solution(N, stages):
    answer=[]
    returnlist = []
    stages.sort() 
    failure={}
    # [1,2,2,2,3,3,4,6]
    for i in range(N):
        try:
            failure[i+1] = stages.count(i+1)/len(stages)
        except ZeroDivisionError:
            failure[i+1] = 0
        stages = stages[stages.count(i+1):]
    returnlist = sorted(failure.items(),reverse = True,key = lambda x:x[1])
    for i,j in returnlist:
        answer.append(i)
    print(answer)
    return answer   

solution(5,[1])
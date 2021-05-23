def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if sum(d[0:i+1]) == budget:
            answer = i+1
            break
        elif sum(d) < budget:
            answer = len(d)
            break
        elif sum(d[0:i+1]) >= budget:
            answer = i
            break
        
    return answer

solution([1],3)
solution([2,2,3,3],10)
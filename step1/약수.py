import math

def solution(left, right):
    answer = 0
    cnt = 0
    binlist=[]
    for i in range(left,right+1,1):
        sqrt = math.sqrt(i)
        if int(sqrt) == sqrt:
            answer -= i
        else:
            answer += i
    return answer

solution(24,27)
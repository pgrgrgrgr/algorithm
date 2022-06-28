from itertools import combinations

def solution(numbers):
    bin=[]
    answer=[]
    bin = list(combinations(numbers,2))
    for i in bin:
        answer.append(sum(i))
    answer = list(set(answer))
    answer.sort()
    return answer

solution([1,230,213,222])

def solution(n):
    answer = 0
    remain = str(n%3)
    result = 0
    while n>2:
        n = n//3
        remain += str(n%3)
    answer = int(remain,3)
    return answer

solution(125)
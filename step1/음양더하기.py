true = True
false = False

def solution(absolutes, signs):
    answer = 0
    while absolutes:
        if signs.pop():
            answer += absolutes.pop()
        else:
            answer -= absolutes.pop()
    return answer

solution([4,7,12],[true,false,true])
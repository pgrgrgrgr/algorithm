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

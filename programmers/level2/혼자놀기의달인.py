def solution(cards):
    answer = 0

    boxes = dict()
    groups = list()

    open = [False] * (len(cards) + 1)
    open_chk = [True] * len(open)
    open_chk[0] = False

    for i in range(1, len(cards) + 1):
        boxes[i] = cards[i - 1]
    
    k = 1
    chk = 1
    group = list()
    while True:
        while not open[k]:
            group.append(k)    
            open[k] = True
            k = boxes[k]
        
        if group:
            groups.append(group)
            group = []

        k = chk + 1
        chk += 1

        if open == open_chk:
            break

    groups.sort(key = lambda x : len(x))

    if len(groups) == 1:
        answer = 1
    else:
        answer = len(groups[-1]) * len(groups[-2])
    return answer

print(solution([8,6,3,7,2,5,1,4,11,13,12,19,14,15,16,18,17,10,9]))
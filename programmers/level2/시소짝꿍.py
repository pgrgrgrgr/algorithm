from collections import defaultdict
from copy import deepcopy

def solution(weights):
    answer = 0
    w_dic = defaultdict(float)

    for w in weights:
        w_dic[w] += 1

    keys = deepcopy(list(w_dic.keys()))

    for w in keys:
        if w_dic[w] > 1:
            answer += (w_dic[w] * (w_dic[w] - 1)) / 2
        answer += w_dic[w * 3/2] * w_dic[w]
        answer += w_dic[w * 4/3] * w_dic[w]
        answer += w_dic[w * 1/2] * w_dic[w]
        answer += w_dic[w * 2/3] * w_dic[w]
        answer += w_dic[w * 3/4] * w_dic[w]
        answer += w_dic[w * 2] * w_dic[w]
        w_dic[w] = 0
    
    return int(answer)

print(solution([100,150,200,200, 1000]))
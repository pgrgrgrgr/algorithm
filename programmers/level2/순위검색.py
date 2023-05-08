from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    dic = defaultdict(list)
    infos = []
    queries = []

    for i in info:
        infos.append(i.split())
    for q in query:
        queries.append(q.replace("and", "").split())

    for i in infos:
        for lang in (i[0], '-'):
            for skill in (i[1], '-'):
                for career in (i[2], '-'):
                    for food in (i[3], '-'):
                        dic[lang + skill + career + food].append(int(i[4]))

    for q in queries:
        tmp = ''.join(q[:-1])
        if tmp in dic:
            idx = bisect_left(sorted(dic[tmp]), int(q[4]))
            answer.append(len(dic[tmp]) - idx)
        else:
            answer.append(0)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], \
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
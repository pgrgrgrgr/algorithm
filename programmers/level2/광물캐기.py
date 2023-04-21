from collections import deque

def solution(picks, minerals):
    if sum(picks) * 5 < len(minerals):
        k = len(minerals) - 5 * sum(picks)
        minerals = minerals[:-k]

    minerals = deque(minerals)
    p_minerals = []
    answer = 0

    while minerals:
        str = ''
        cost = 0
        for _ in range(5):
            if not minerals:
                break
            mineral = minerals.popleft()
            if mineral == "diamond":
                cost += 25
                str += 'd'
            elif mineral == "iron":
                cost += 5
                str += 'i'
            else:
                cost += 1
                str += 's'
        p_minerals.append([str, cost])
        str = ''
        cost = 0

    p_minerals.sort(key = lambda x: -x[1])
    print(p_minerals)
    p_minerals = deque(p_minerals)

    while picks[0] and p_minerals:
        answer += len(p_minerals[0][0])
        picks[0] -= 1
        p_minerals.popleft()

    while picks[1] and p_minerals:
        for m in p_minerals[0][0]:
            if m == 'd':
                answer += 5
            else:
                answer += 1
        picks[1] -= 1
        p_minerals.popleft()

    while picks[2] and p_minerals:
        for m in p_minerals[0][0]:
            if m == 'd':
                answer += 25
            elif m == 'i':
                answer += 5
            else:
                answer += 1
        picks[2] -= 1
        p_minerals.popleft()

    return answer

print(solution([1, 0, 1], ["iron", "iron", "iron", "iron", "iron", "diamond", "diamond"]))
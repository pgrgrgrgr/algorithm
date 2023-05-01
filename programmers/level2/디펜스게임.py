from collections import deque
from queue import PriorityQueue

def solution(n, k, enemy):
    answer = 0
    enemy = deque(enemy)
    p_enemy = PriorityQueue()
    
    while enemy:
        e = enemy.popleft()
        n -= e
        p_enemy.put((-e, e))
        
        if not k and n < 0:
            break

        if n >= 0:
            answer += 1
        elif n < 0:
            k -= 1
            n += p_enemy.get()[1]
            answer += 1

    return answer

print(solution(10, 1, [10, 2, 2, 2, 2, 2]))

# 5, 3, 5, 5, 5
from collections import deque

def solution(storey):
    answer = 0
    tmp = deque(list(str(storey)))
    q = deque()

    while tmp:
        q.append(int(tmp.popleft()))
    
    while q:
        v = q.pop()
        if not q:
            if v > 5:
                answer += 10 - v
                answer += 1
            else:
                answer += v    
            break
        if v > 5:
            answer += 10 - v
            if q:
                q[-1] += 1
            if v == 10 and not q:
                answer += 1
        elif v == 5:
            if not q:
                answer += v
            else:
                answer += v
                if q[-1] >= 5:
                    q[-1] += 1
        else:
            answer += v
    
    return answer

solution(7554) #9992 -> 999 -> 99 10 -> 9 10 -> 10 -> 0
# 5560 (5)
# 5600(4)
# 6000(3)
# 0(4 + 1)
# 4450 (5)
# 4500 (5)
# 5000 (5)
# + 5
# 9972 ->(2) 9870 ->(3) 10000 ->(1) 0
# 9 9 7 2 ->(2) 9 9 7 ->(3) 9 10     ->(1) 10 ->
# 5554 -> 5550 -> 5600
# 9392 ->(2) 9390 ->(1) 9400 ->(4) 9000 ->(1) 10000 ->(9) 0
# 9392 -> 9390 -> 9400 ->(6) 10000 -> 0
# 10000

# 392
# 100
# 92
# 100
# 2
# 0
# 8

# 6425
# 1 0 9 9 -> 1 0 10 -> 
# 922
# 920
# 900

import math

def solution(r1, r2):
    answer = 0
    qt = 0

    for x in range(1, r2):
        if x < r1:
            down = math.ceil(math.sqrt(r1 * r1 - x * x))
            up = math.floor(math.sqrt(r2 * r2 - x * x))
            qt += (up - down + 1)
        else:
            down = 1
            up = math.floor(math.sqrt(r2 * r2 - x * x))
            qt += up - down + 1
    
    answer = 4 * qt + 4 * (r2 - r1 + 1)
    
    return answer

print(solution(2, 3))
from collections import deque

def solution(n, computers):    
    answer = 0
    visited = [False for _ in range(n)]
    
    def dfs(idx):
        visited[idx] = True
        for com in range(n):
            if computers[idx][com] and not visited[com]:
                dfs(com)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer

solution(4, [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]])
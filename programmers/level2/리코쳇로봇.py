from collections import deque

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

def in_grid(board, x, y):
    return 0 <= x < len(board) and 0 <= y < len(board[0])

def init(board):
    grid = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                grid[i][j] = 0
            elif board[i][j] == 'D':
                grid[i][j] = 1
            elif board[i][j] == 'G':
                grid[i][j] = 2
            elif board[i][j] == 'R':
                grid[i][j] = 3
                robot = [i, j]

    return grid, robot

def bfs(board, robot):
    visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    visited[robot[0]][robot[1]] = 1
    
    q = deque()
    q.append(robot)

    while q:
        cur_x, cur_y = q.popleft()
        if board[cur_x][cur_y] == 2:
            return visited[cur_x][cur_y]
        
        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy
            while in_grid(board, nx, ny) and board[nx][ny] != 1:
                nx, ny = nx + dx, ny + dy
            nx, ny = nx - dx, ny - dy

            if not visited[nx][ny]:
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                q.append([nx, ny])

    return -1

def solution(board):
    grid, robot = init(board)
    answer = bfs(grid, robot)
    
    return answer - 1 if answer > 0 else -1

solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])
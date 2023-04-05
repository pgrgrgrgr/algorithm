N, Q = map(int, input().split())
size = 2 ** N
grid = [list(map(int, input().split())) for _ in range(size)]
L = list(map(int, input().split()))

print(grid)
print(grid[0:1][0:1])
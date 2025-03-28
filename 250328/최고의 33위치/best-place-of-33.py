n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def f(n, grid):
    cnt = 0
    for i in range(n-2):
        for j in range(n-2):
            sumGrid = sum(grid[j][i:i+3]) + sum(grid[j+1][i:i+3]) + sum(grid[j+2][i:i+3])
            cnt = max(cnt, sumGrid)
    return cnt


print(f(n, grid))

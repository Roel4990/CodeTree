n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
if m == 1:
    print(2*n)
else:
    answer = 0
    for i in range(n):
        cnt = 1
        a = grid[i][0]
        for j in range(1, n):
            if a == grid[i][j]:
                cnt += 1
                if m == cnt:
                    answer += 1
                    break
            else:
                cnt = 1
                a = grid[i][j]
    for i in range(n):
        cnt = 1
        a = grid[0][i]
        for j in range(1, n):
            if a == grid[j][i]:
                cnt += 1
                if m == cnt:
                    answer += 1
                    break
            else:
                cnt = 0
                a = grid[j][i]
    print(answer)
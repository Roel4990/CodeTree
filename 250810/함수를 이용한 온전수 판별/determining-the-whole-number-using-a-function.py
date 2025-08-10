a, b = map(int, input().split())

# Please write your code here.
cnt = 0
for i in range(a, b+1):
    if i % 2 != 0 and i % 5 != 0 and (i%3 != 0 or i%9 == 0):
        cnt += 1

print(cnt)
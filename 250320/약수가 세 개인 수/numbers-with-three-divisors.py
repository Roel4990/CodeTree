start, end = map(int, input().split())

# Please write your code here.
cnt = 0
for i in range(start, end+1):
    cntCheck = 0
    for j in range(1, i+1):
        if i % j == 0:
            cntCheck += 1
    if cntCheck == 3:
        cnt += 1
print(cnt)

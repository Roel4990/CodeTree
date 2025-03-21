cnt = 0
for i in range(4):
    nList = list(map(int, input().split()))
    for j in nList:
        if j % 5 == 0:
            cnt += 1
print(cnt)
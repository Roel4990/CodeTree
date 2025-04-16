n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.

# 평균 구하기
avg = sum(blocks)//n
cnt = 0

for i in blocks:
    if avg > i:
        cnt += avg - i

print(cnt)        
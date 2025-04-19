n = int(input())
studentScore = [list(map(int, input().split())) for i in range(n)]

cnt = 0
for i in studentScore:
    if sum(i) // len(i) >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")
print(cnt)
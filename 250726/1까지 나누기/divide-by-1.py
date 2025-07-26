N = int(input())
cnt = 1
while True:
    if N == 1:
        print(cnt + 1)
        break
    N //= cnt
    if N < 1:
        print(cnt)
        break
    cnt += 1

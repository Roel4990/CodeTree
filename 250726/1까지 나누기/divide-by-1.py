N = int(input())
cnt = 1
while True:
    N //= cnt
    if N < 1:
        print(cnt)
        break
    cnt += 1

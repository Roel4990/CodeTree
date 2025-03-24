n = int(input())

# Please write your code here.
def f(N, cnt):
    if N == 1:
        return cnt
    cnt += 1
    return f(N // 2, cnt) if N % 2 == 0 else f(N*3+1, cnt)

print(f(n, 0))
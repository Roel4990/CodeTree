N = int(input())

# Please write your code here.
cnt = 0
def f(n):
    if n == 1:
        return
    global cnt 
    cnt += 1
    if n % 2 == 0:
        return f(n//2)
    else:
        return f(n//3)

f(N)
print(cnt)

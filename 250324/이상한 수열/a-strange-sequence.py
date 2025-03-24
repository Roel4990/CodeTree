N = int(input())

# Please write your code here.

def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return f(n-1) + n//3

print(f(N))
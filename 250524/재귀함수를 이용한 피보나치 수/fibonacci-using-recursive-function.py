N = int(input())

# Please write your code here.

def f(n):
    if n <= 2:
        return 1
    return f(n - 2) + f(n - 1)

print(f(N))
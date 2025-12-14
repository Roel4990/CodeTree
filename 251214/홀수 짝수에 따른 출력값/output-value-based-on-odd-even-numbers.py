N = int(input())

# Please write your code here.
def f(n):
    if n == 1 or n == 2:
        return n
    return n + f(n-2)

print(f(N))

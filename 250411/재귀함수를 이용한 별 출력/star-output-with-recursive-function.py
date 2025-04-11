n = int(input())

# Please write your code here.
def f(n):
    if n < 1:
        return
    print("*" * (6 - n))
    f(n-1)

f(n)
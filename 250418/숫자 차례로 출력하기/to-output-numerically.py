n = int(input())

# Please write your code here.

def f(a):
    if a > n:
        print()
        return
    print(a, end=" ")
    f(a+1)
    print(a, end=" ")


f(1)
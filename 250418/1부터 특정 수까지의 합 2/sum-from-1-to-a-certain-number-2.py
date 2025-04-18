N = int(input())

# Please write your code here.
def add(n):
    if n == 1: return 1
    return add(n-1) + n


print(add(N))
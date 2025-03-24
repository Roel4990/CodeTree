a, b, c = map(int, input().split())

# Please write your code here.
def result(n):
    if n == 0:
        return 0
    return n%10 + result(n//10) 

print(result(a*b*c))

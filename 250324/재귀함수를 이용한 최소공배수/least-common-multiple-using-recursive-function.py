n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import math

def lcm(x, y):
    return x * y // math.gcd(x, y)

def f(Arr):
    if len(Arr) == 1:
        return Arr[0]
    Arr.append(lcm(Arr.pop(), Arr.pop()))
    return f(Arr)

print(f(arr))
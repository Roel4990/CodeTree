a, b = map(int, input().split())
n = input()

# Please write your code here.
decimal = int(n, a)

if b == 2:
    print(bin(decimal)[2:])
elif b == 8:
    print(oct(decimal)[2:])
elif b == 16:
    print(hex(decimal)[2:])
else:
    result = ""
    while decimal > 0:
        result = str(decimal % b) + result
        decimal //= b
    print(result)

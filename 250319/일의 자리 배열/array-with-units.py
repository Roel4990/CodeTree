a, b = map(int, input().split())

print(a, b, end=" ")

for i in range(8):
    if a + b >= 10:
        print((a+b)%10, end=" ")
        a, b = b, (a+b)%10
    else:
        print(a+b, end=" ")
        a, b = b, a+b
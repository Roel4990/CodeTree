M, D = map(int, input().split())

# Please write your code here.
if M <= 7:
    if M % 2 == 1:
        print("Yes" if D <= 31 else "No")
    else:
        if M == 2:
            print("Yes" if D <= 28 else "No")
        else:
            print("Yes" if D <= 30 else "No")
elif M <= 12:
    if M % 2 == 0:
        print("Yes" if D <= 31 else "No")
    else:
        print("Yes" if D <= 30 else "No")
else:
    print("No")
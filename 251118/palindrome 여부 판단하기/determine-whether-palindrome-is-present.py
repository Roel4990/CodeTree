A = input()

# Please write your code here.
AList = list(A)
reservedAList = list(reversed(AList))
print("Yes" if AList == reservedAList else "No")
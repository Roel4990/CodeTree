A = input()

# Please write your code here.
cnt = 0
for i in range(len(A)):
    for j in range(len(A)):
        if A[i] != ")" and i < j and A[j] == ")":
            cnt += 1

print(cnt)
A = input()
n = len(A)
# Please write your code here.
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if A[i] == '(' and A[j] == ')':
            cnt += 1

print(cnt)
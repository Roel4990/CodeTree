a, b = map(int, input().split())

# Please write your code here.
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
cnt = 0
for i in range(a, b):
    if is_prime_number(i):
        if sum(list(map(int, str(i)))) % 2 ==0:
            cnt+=1

print(cnt)


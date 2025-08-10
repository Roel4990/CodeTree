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
        digit_num = sum([int(num) for num in str(i)])
        if digit_num % 2 == 0:
            cnt += 1

print(cnt)


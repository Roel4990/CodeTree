n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.


def f(arr, maxNum):
    if len(arr) == 0:
        return maxNum
    num = arr.pop(0) + arr.pop()
    if maxNum < num:
        maxNum = num
    return f(arr, maxNum)

nums.sort()

print(f(nums, 0))
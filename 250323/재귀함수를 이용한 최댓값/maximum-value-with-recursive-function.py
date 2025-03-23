n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def find_max(lst, index=0):
    if index == len(lst) - 1:
        return lst[index]

    max_of_rest = find_max(lst, index + 1)
    if lst[index] > max_of_rest:
        return lst[index]
    else:
        return max_of_rest

print(find_max(arr))
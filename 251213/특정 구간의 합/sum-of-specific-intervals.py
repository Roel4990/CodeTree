n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
for query in queries:
    # if query[1] == len(arr):
    #     print(sum(arr[query[0]-1:]))
    # else:
    print(sum(arr[query[0]-1: query[1]]))
    
MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
maxNum = min(scores)

index = scores.index(maxNum)

print(codenames[index], scores[index])
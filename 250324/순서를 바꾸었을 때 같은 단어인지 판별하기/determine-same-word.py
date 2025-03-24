word1 = input()
word2 = input()

# Please write your code here.
def f(word1, word2):
    wordList1 = sorted(list(word1))
    wordList2 = sorted(list(word2))
    return wordList1 == wordList2

print("Yes" if f(word1, word2) else "No")
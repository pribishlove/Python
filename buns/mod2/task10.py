words = input().split(" ")
for word in words:
    print(word[len(word)-1], end='')
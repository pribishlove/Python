words = input()
resultStr = ""
for i in range(0, len(words)):
    if words[i] == " ":
        resultStr += words[i-1]
    elif i == len(words) - 1:
        resultStr += words[i]
    else:
        continue
print(resultStr)

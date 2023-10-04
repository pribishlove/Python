s = input()
currentStr = ""
for i in range (len(s)-1, -1, -1):
    if s[i] == ".":
        print(currentStr[::-1])
        currentStr = ""
    else:
        currentStr += s[i]
print(currentStr)

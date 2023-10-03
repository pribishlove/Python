s = input()
newStr = ""
for i in s:
    if i != " " and i != ")" and i != "(" and i != "-":
        newStr += i
print(newStr)
str = input()
s = ""
i = ""
countSpace = 0
for k in range(0, len(str)):
  if str[k]!="," and countSpace == 0:
    s += str[k]
  elif str[k]!="," and countSpace == 1:
    i += str[k]
  else:
    countSpace += 1
count = 0
for j in s:
    if j == i:
        count += 1
    else:
        print(count)
        break

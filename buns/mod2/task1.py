s = input()
a = ""
b = ""
countSpace = 0
for i in range(0, len(s)):
  if s[i]!=" " and countSpace == 0:
    a += s[i]
  elif s[i]!=" " and countSpace == 1:
    b += s[i]
  else:
    countSpace += 1
print(a%b)

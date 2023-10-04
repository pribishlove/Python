s = input()
char = ""
delta = ""
countSpace = 0
for i in range(0, len(s)):
  if s[i]!="," and countSpace == 0:
    char += s[i]
  elif s[i]!="," and countSpace == 1:
    delta += s[i]
  else:
    countSpace += 1
delta = int(delta)
print(chr(97 + ((ord(char) - 97) + delta)% 26))

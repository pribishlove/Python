s = input()
a = ""
b = ""
c = ""
countSpace = 0
for i in range(0, len(s)):
    if s[i]!=" " and countSpace == 0:
        a += s[i]
    elif s[i]!=" " and countSpace == 1:
        b += s[i]
    elif s[i]!=" " and countSpace == 2:
        c += s[i]
    else:
        countSpace += 1
a = int(a)
b = int(b)
c = int(c)
if a > b:
    if b > c:
        print(b)
    elif a > c:
        print(c)
    else:
        print(a)
elif a>c:
    print(a)
elif b>c:
    print(c)
else:
    print(b)

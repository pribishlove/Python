s = input()
sumOdd = 0
sumEven = 0
for i in range(0,len(s)):
    if i % 2 != 0:
        sumEven += int(s[i])
    else:
        sumOdd += int(s[i])
if (sumEven * 3 + sumOdd) % 10 == 0:
    print("yes")
else:
    print("no")
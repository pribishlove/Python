s = input()
k0 = 0
k1 = 0
for i in s:
    if i == "0":
        k0 += 1
    else:
        k1 += 1
if k0 == k1:
    print("yes")
else:
    print("no")
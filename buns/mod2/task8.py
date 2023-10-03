s, i = input().split(", ")
count = 0
for j in s:
    if j == i:
        count += 1
    else:
        print(count)
        break
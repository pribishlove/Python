a = input().split(" ")
b = set(a)
if len(b) == 1:
    print("Все числа равны")
elif len(b) > 1 and len(b) < len(a):
    print("Есть равные и неравные числа")
else:
    print("Все числа разные")
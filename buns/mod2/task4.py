#a - число, которое нужно перевести
#x - в какую систему счисления надо перевести
def transfer(a, x):
    s = ""
    while a > 0:
        if a%x == 10:
            s += "A"
        elif a%x == 11:
            s += "B"
        elif a%x == 12:
            s += "C"
        elif a%x == 13:
            s += "D"
        elif a%x == 14:
            s += "E"
        elif a%x == 15:
            s += "F"
        else:
            s += str(a%x)
        a//=x
    return s

a = int(input())

if a<=0:
    print("Неверный ввод")
else:
    print(transfer(a,2)[::-1], transfer(a,8)[::-1], transfer(a,16)[::-1])
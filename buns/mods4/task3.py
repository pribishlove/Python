def evklid(a,b):
    if a == b:
        return a
    elif a > b:
        return evklid(a-b,b)
    else:
        return evklid(a,b-a)
print(evklid(int(input()),int(input())))
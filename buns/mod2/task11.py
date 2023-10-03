def Dublicates():
    s = input().replace(" ", "")
    if len(s) > 10:
        return True
    for i in range(0, len(s)):
        for k in range(0, len(s)):
            if i != k and s[i] == s[k]:
                return True
    return False
print(Dublicates())
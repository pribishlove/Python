consonantLetter = "бвгджзйклмнпрстфхцчшщ"
vowelLetter = "аеёиоуыэюя"
s = input()
countVowel = 0
countConstonant = 0
for i in s:
    if i in vowelLetter:
        countVowel += 1
    elif i in consonantLetter:
        countConstonant += 1
    else:
        continue
print(countVowel, countConstonant)
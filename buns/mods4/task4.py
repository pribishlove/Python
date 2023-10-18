def is_palindrome_possible(word):
    if len(set(word)) == len(word) // 2 or len(set(word)) == len(word) // 2 + 1:
        return True
    else:
        return False
def create_palindrome(word):
    if is_palindrome_possible(word):
        letter_count = {}
        palindrome = []
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        middle_letter = ''
        for letter, count in letter_count.items():
            if count % 2 != 0:
                middle_letter = letter
            palindrome.extend([letter] * (count // 2))
        palindrome = palindrome + [middle_letter] + list(reversed(palindrome))
        return ''.join(palindrome)
    else:
        return "Палиндром невозможен"

word = input()
if is_palindrome_possible(word):
    palindrome = create_palindrome(word)
    print(palindrome)
else:
    print("Палиндром невозможен")
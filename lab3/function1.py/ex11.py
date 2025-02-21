def check_palindrome(word):
    reverse_word = word[::-1]
    if reverse_word == word:
        print(f"{word} is palindrome")
    else:
        print(f"{word} is not palindrome")

word = str(input("word: "))
check_palindrome(word)
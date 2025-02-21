def word_reverse(words):
    words = list(words.split())
    words.reverse()
    for i in words:
        print(i , end = " ")

words = str(input())
word_reverse(words)




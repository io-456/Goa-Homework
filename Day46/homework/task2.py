def long_words(word):
    long_word = []
    for i in word:
        if len(i) > 5:
            long_word.append(i)
    return long_word        

words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'grapefruit']

result = long_words(words)

print(result)
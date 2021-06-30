'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''
with open("words.txt", "r+") as f:
    words = f.readlines()
    text = []
    words_updated = [i.strip() for i in words]
    print(words_updated)
    for word in words_updated:
        if len(word) > 20:
            text.append(word.strip())
    print(text)


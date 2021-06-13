'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''
with open("words.txt", "r") as f:
    print(f.readlines())
    text = []
    for i in f:
        if len(i) > 20:
            text.append(i.strip())
    print(text)


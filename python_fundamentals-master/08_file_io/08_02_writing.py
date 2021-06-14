'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

f_list = []
with open("words.txt", "r") as f_order:
    words = f_order.readlines()
    print(words)

with open("words_reverse.txt", "w") as f_reversed:
    words.reverse()
    # words = [i.strip() for i in words]
    for word in words:
        f_reversed.write(word)


    #         = f_list[::-1]
    # f_reversed.write(f"{f_reversed_list})


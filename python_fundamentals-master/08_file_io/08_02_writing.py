'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

f_list = []
with open("words.txt", "r") as f_order:
    words = f_order.readlines()
    print(words)

with open("words_reverse.txt", "w") as f_reversed:
    f_reversed = words.reverse()
    print(f_reversed.strip())


    #         = f_list[::-1]
    # f_reversed.write(f"{f_reversed_list})


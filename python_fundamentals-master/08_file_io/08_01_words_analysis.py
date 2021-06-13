'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
f = open("words.txt" , "r")
# print(f.readlines())


word_min = "hello"
word_max = ""
words_min = []
words_max = []
total_num_words = 0


#not great, as it will not give the tie for word_max:
for word in f:
    if len(word) <= len(word_min):
        word_min = word
        words_min.append(word_min.strip())
    if len(word) >= len(word_max):
        word_max = word
    total_num_words += 1

print(words_min)
print(word_max)
print(total_num_words)

f.close()
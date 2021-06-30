'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
with open("words.txt" , "r+") as f:
    len_word_min = float("inf")
    word_max = 0
    word_max_len = 0
    words_min = []
    words_max = []
    total_num_words = 0


    for word in f:
        word = word.strip()
        len_word = len(word)
        if len_word < len_word_min:
            len_word_min = len_word
            words_min = [word]
        elif len_word == len_word_min:
            words_min.append(word)
        elif len_word == word_max_len:
            words_max.append(word)
        elif len_word > word_max_len:
            words_max = [word]
            word_max_len = len_word
        total_num_words += 1

    print(words_min)
    print(words_max)
    print(total_num_words)

#Debugger is great :D

# g = ["hello", "high", "bab", "flight", "ba", "da", "to"]
# len_word_min = float('inf')
# word_max = ""
# word_max_len = 0
# words_min = []
# words_max = []
# total_num_words = 0
#
# for word in g:
#     if len(word) <= len_word_min:
#         len_word_min = word
#         words_min.append(len_word_min.strip())
#     if len(word) == word_max_len:
#         words_max.append(word)
#     elif len(word) > word_max_len:
#         words_max = [word]
#         word_max_len = len(word)
#     total_num_words += 1
#
# print(words_min)
# print(words_max)
# print(total_num_words)


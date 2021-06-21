'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
with open("words.txt" , "r+") as f:
    word_min = str("inf")
    word_max = ""
    word_max_len = 0
    words_min = []
    words_max = []
    total_num_words = 0

    for word in f:
        if len(word) <= len(word_min):
            word_min = word
            words_min.append(word_min.strip())
        if len(word) == word_max_len:
            words_max.append(word)
        elif len(word) > word_max_len:
            words_max = [word]
            word_max_len = len(word)
        total_num_words += 1

    print(words_min)
    print(words_max)
    print(total_num_words)

#Debugger is great :D
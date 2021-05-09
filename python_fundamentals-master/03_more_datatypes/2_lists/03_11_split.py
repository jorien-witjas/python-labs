'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

x = "the cow is dancing on the table"
y = x.split()
print(y)
longest = ""
for word in y:
    if len(word) > len(longest):
        longest = word
    else: continue
print(longest)


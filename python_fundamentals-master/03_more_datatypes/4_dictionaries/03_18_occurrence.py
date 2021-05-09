'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
new_dict = {}
sentence = "Saturdaymorning"
unique_char = ()

for element in sentence:
    if element not in sentence:
        unique_char.append(element)
    occurence = sentence.count(element)

    new_dict[element] = occurence
print(new_dict)


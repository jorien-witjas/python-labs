'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = []
for item in list_:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)

#2nd try
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = set(list_)
print(unique_list)

#correct:
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = []
for item in list_:
    if list_.count(item) == 1:
        unique_list.append(item)
print(unique_list)


#MINI LAB CIPHER CODE ENCRIPTING

secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
secret = secret.lower()
cipher = 7
alpha = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

list_secret = []
list_alpha = []

for item in secret:
    list_secret.append(item)
print(list_secret)

for item in alpha:
    list_alpha.append(item)
print(list_alpha)

code_alpha = alpha[cipher:] + alpha[0:cipher]
new_letter = ""
for letter in list_secret:
    if letter in list_alpha:
          new_letter += alpha[(alpha.find(letter) + cipher)]
          print(new_letter)
    else:
        new_letter += letter



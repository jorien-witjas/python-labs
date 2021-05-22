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
    else:
        new_letter += letter
print(new_letter)

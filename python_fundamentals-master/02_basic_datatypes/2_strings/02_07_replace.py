'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

x = "hi there"
y = "&"
a = x[0]
z = x.replace(a,y)
print(z)

fruit = ["banana","pineapple","apple"]
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1


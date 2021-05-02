'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
x = input("Please give me a word: ")
y = input("Please give me another word: ")
z = input("Please give me a third word: ")

print(len(x),",",x)
print(len(y),",",y)
print(len(z),",",z)

#challenge
if len(x) > len(y) and len(z):
    print(x)
elif len(y) > len(x) and len(z):
    print(y)
else:
    print(z)

#Comment/question: what happens if you code if len(x) > len(y) and len(z) == True: ?? If I try that then it will print "print(z)"

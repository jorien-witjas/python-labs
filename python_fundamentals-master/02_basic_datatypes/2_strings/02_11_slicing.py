'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

name = input("please state your name: ")

print(name[1:]+name[0]+"ay")


#question: is it true that you can only .append() a list?
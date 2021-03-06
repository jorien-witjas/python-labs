'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
#trying to get user input into a list:
# x = (input("enter a series of 10 numbers divided by a space: "))
# x.split()
# print(x)
# this is not the  right way. But skipping this for now.

#exercise
x = [2, 3, 56, 645, 78, 3, 9, 97, 34, 450]
a = max(x)
print(a)

#practice without using max()
largest_num = 0
for number in x:
    if number > largest_num:
        largest_num = number
print(largest_num)

#challenge:
product = 1
for number in x:
    y = product*number
    product = y
print(product)
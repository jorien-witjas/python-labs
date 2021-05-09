'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
#sort numbers from a list of numbers:
numbers_list = [3, 4, 5, 6, 7, 135, 76, 889, 2]
new_numbers_list = sorted(numbers_list)
print(new_numbers_list)
hallo = str(new_numbers_list)
print(hallo)

#WRONGstores numbers in tuples of two is a list:
update_list = []
for num in hallo:
    tuple(num)
    update_list.append(num)
print(update_list)

#stores numbers in tuples of two is a list:
numbers_list = [3, 4, 5, 6, 7, 135, 76, 889, 2]
new_numbers_list = sorted(numbers_list)
print(new_numbers_list)

update_list = []
for i in new_numbers_list:
    slice = tuple(new_numbers_list(len(2)))
    update_list.append(slice)
print(update_list)

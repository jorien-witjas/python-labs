'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
input = "Tomorrow it will be sunny outside"
#make input into list with two items
my_input_list = input.split()

print(my_input_list)

#make each item of my_input_list into a tuples
y = []
for item in my_input_list:
    tuple(item)
    y.append(tuple(item))
print(y)






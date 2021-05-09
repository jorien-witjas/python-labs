'''
Write a script that "flattens" a shallow list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Note that your input list only contains one level of nested lists.
This is called a "shallow list".

CHALLENGE: Do some research online and find a solution that works
to flatten a list of any depth. Can you understand the code used?

for loop to interate over elements,and if statement to see if the element is an element or a (new) list.
If element, append to flat list, if list then "go back into for loop (w/ function).
'''

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = []
for item in starting_list:
    flattened_list += item
print(flattened_list)


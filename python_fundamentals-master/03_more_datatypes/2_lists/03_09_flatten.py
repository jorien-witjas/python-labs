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

# challenge-- new lists to flatten:
start_list_1 = [[1,2,3],'hi',[1,2,3]]
flattened_list = []
for item in start_list_1:
    if isinstance(item, str):
        flattened_list.append(item)
    else:
        flattened_list += item
print(flattened_list)

#another list with multiple nests - it will go over every item, but does not unpack the 'second  layer' list
start_list_2 = [[1,2,3],4,5,[6,7,[8,9],2]]
flattened_list = []
for item in start_list_2:
    if isinstance(item, int):
        flattened_list.append(item)
    else:
        flattened_list += item
print(flattened_list)



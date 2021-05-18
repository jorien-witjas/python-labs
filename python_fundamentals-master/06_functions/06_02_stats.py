'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]
#Smallest didn't work:
# def stats(argument):
#     longest_item = 0
#     smallest_item = 0
#     argument_sum = 0
#     count = 0
#     for item in argument:
#         if item > longest_item:
#             longest_item = item
#     for item in argument:
#         if item < smallest_item:
#             smallest_item = item
#     for item in argument:
#         argument_sum += item
#         count += 1
#     argument_av = (argument_sum / count)
#     return longest_item, smallest_item, argument_sum, argument_av
# print(stats(example_list))

#can i reduce the for loops to have everthing in one loop?


def stats(argument):
    longest_item = 0
    smallest_item = argument[0]
    argument_sum = 0
    count = 0
    for item in argument:
        if item > longest_item:
            longest_item = item
    for item in argument:
        if item < smallest_item:
            smallest_item = item
    for item in argument:
        argument_sum += item
        count += 1
    argument_av = (argument_sum / count)
    return longest_item, smallest_item, argument_sum, argument_av
print(stats(example_list))
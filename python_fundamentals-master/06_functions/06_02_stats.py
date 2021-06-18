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


def stats(list_of_numbers):
    print(list_of_numbers)
    largest_item = list_of_numbers[0]
    smallest_item = list_of_numbers[0]
    argument_sum = 0
    count = 0
    for item in list_of_numbers:
        if item > largest_item:
            largest_item = item
        if item < smallest_item:
            smallest_item = item
        argument_sum += item
        count += 1
    argument_av = (argument_sum / count)
    list_of_numbers.append(largest_item)
    return [largest_item, smallest_item, argument_sum, argument_av]


print(stats)

a = stats
print(a(example_list))
print(stats(example_list))
print(stats(a(example_list)))

print(example_list)

hello = "good morning"
def practice_function(string):
    string += "how did you sleep"
    return string

print(practice_function(hello))
print(hello)

# side effects if you update a list inside a function and forget that the list is mutable.

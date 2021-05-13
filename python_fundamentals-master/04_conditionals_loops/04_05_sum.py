'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''

number_1 = 1
number_2 = 100
sum_number = 0
for num in range(number_1, number_2 + 1):
    sum_number += num
print(sum_number)

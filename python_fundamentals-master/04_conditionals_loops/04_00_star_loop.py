'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = int(input("please enter a number: "))
for n in range(n):
    print("*" * n)

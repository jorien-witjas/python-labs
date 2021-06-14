'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''
try:
    with open("integers.txt", "r+") as ints:
        ints_read = ints.read()
except FileNotFoundError:
    print("the file does not exist, please create first")
except ValueError:
    print("there are strings in your file, I can't calculate with those. Please make sure your file only has integers")
else:
    num_1 = ints.readline(1)        #ValueError - file closed?
    num_2 = ints.readline(2)
    print(f"Sum of your integers is {num_1 + num_2}")



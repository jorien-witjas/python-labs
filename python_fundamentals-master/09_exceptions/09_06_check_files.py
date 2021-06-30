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
    # num_1 = ints.readline(1)        #ValueError - file closed?
    # num_2 = ints.readline(2)
    # print(f"Sum of your integers is {num_1 + num_2}")
    ints_read = [i.strip() for i in ints_read]
    num_1 = ints_read[0]
    num_2 = ints_read[4]   # the integers file has 1,2,3,4,5 on different lines. However when I read [1] it gives me nothing and when i read [2] it gives me 2. [3] is nothing and [4] is 3.
    print(num_1)
    print(num_2)
    print(f"Sum of your integers is {int(num_1) + int(num_2)}")



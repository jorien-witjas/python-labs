'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
amount = int(input("Enter your investment amount: "))
interest = int(input("Enter your interest rate in percentage: "))
time = int(input("Enter the numbers of years you will be investing: "))

print("Your future value is: ", amount + interest + time)

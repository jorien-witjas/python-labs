'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
tests should pass. Also include a test that does not pass.

NOTE: You can write both the code as well as the tests for it in this single file.
However, feel free to adhere to best practices and separate your tests and the functions you are testing
into different files. Note that you will run into an error when attempting to import this file,
because Python modules can't begin with a number.

'''
#
def get_email(f_name, l_name, domain):
    email = f_name + l_name + "@" + domain
    return email

if __name__ == '__main__':
    f_name = "gilad"
    l_name = "gressel"
    domain = "hotmail.com"
    mail_gilad = get_email(f_name,l_name,domain)
    print(mail_gilad)
'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
list_1 = [1,2,3,4,5,6,7,8,9,10]
def function_1(argument_1):
    list_2 = argument_1[1:3]
    return list_2

def function_2(argument_2):
    new_list = [4,5,6]
    for item in function_1(list_1):
        new_list.append(item)
    return new_list

def function_3(argement_3):
    if function_2 != 0:
        today = print("this is working well")
        return today
#why does function_3 end with none?

print(function_1(list_1))
print(function_2(list_1))
print(function_3(list_1))

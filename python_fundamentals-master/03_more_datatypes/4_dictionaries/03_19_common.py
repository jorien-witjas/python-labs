'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

'''#not right, because you will loose the duplicates from the original dict
dict_1.update(dict_2)
print(dict_1)
'''

#using for loop, but missing dict_2 only entry
# for k in dict_1:
#     if k in dict_2:
#        dict_1[k] = dict_1[k] + dict_2[k]
# print(dict_1)
#
# new_dict = {}
# for k in dict_2:
#     if k not in dict_1:
#         new_dict.update(dict_2[k])
# print(new_dict)
#
# result = dict_1 + new_dict

dict_3 = {}
for k in dict_1:
    if k in dict_2 or dict_1:
        dict_3[k] = (dict_1.items() + dict_2.items())
print(dict_3)
#
# for k in dict_2:
#     if k not in dict_1:
#         dict_3[k] = dict_2[k]
#     elif k in dict_1:
#         dict_3[k] = dict_1[k] + dict_2[k]
#
# print(dict_3)
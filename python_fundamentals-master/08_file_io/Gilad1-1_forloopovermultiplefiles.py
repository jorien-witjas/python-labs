list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = [10,11,12,13,14,15,16,17]
list_3 = [100,101,204,506]
combined_files = zip(list_1,list_2,list_3)
new_list = []
for item in zip(list_1,list_2,list_3):
    new_list.append(item)
print(new_list)

final_list = [item[0] for item in zip(list_1,list_2,list_3)]  #list comprehension
print(final_list)
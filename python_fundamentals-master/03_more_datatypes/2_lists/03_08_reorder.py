'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1


first try:
count = 0
x = [10, 21, 3, 43, 15, 87, 7, 811, 9, 10]
for i in x:
    if count % 2 == 1:
        print(i)
    count += 1

count = 10
for i in x:
    if count % 2 == 0:
        print(i)
    count -= 1
'''


# x = [10, 21, 3, 43, 15, 87, 7, 811, 9, 10]
# count = 0
# for i in x:
#     if count % 2 == 1:
#         print(i, end=" ")
#     count += 1
# x.reverse()
# count = 0
# for i in x:
#     if count % 2 == 1:
#         print(i, end=" ")
#     count +=1

#try after some Gilad-input :)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
updated_x = x[1::2] + x[-2::-2]
print(updated_x)
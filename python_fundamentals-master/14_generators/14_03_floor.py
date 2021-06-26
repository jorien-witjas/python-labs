'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''


gen = (x for x in range(1000))

for i in gen:
    q = i // 1111
    print(q)



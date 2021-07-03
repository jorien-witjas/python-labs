'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

seasons = ["summer", "autumn", "winter", "spring"]
for c, s in enumerate(seasons):
    print(c, s)

count = 0
for s in seasons:
    print(count, s)
    count += 1

a = enumerate(seasons)

def calculation(x):
    x+=1
    yield x

x = 4
print(calculation(x))

def alphabet():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for a in alpha:
        yield a


a = alphabet()
print(a.__next__())
print(a.__next__())


def even_items(iterable):
    return [v for i, v in enumerate(iterable, start=1) if not i % 2]

def even_items_2(iterable):
    list_1 = []
    for i,v in enumerate(iterable, start=1):
        if i % 2 == 0:
            list_1.append(v)
    return list_1
#
print(even_items(alphabet()))

print(even_items_2(alphabet()))


def my_function(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

my_function(item1 = "hi", item2 = "hello")
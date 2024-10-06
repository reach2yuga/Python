'''List
List comprehension offers one-liner syntax to create a new list based on the values of the existing list. You can use a `for loop` to replicate the same thing, but it will require you to write multiple lines, and sometimes it can get complex. 

List comprehension eases the creation of the list based on existing iterable. '''


my_list = [i for i in range(1, 10)]
my_list
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


'''Dictionary
Similar to a List comprehension, you can create a dictionary based on an existing table with a single line of code. You need to enclose the operation with curly brackets `{}`.
'''

my_dict = {i for i in range(1, 10)}
my_dict
# {1, 2, 3, 4, 5, 6, 7, 8, 9}

'''Tuple
It is a bit different for Tuples. You can create Tuple comprehension using round brackets `()`, but it will return a generator object, not a tuple comprehension.

You can run the loop to extract the elements or convert them to a list.'''


my_tuple = (i for i in range(1, 10))
my_tuple
# <generator object <genexpr> at 0x7fb91b151430>
#difference between a mutable data type and an immutable data type

'''Mutable data types:
Definition: Mutable data types are those that can be modified after their creation.
Examples: List, Dictionary, Set.
Characteristics: Elements can be added, removed, or changed.
Use Case: Suitable for collections of items where frequent updates are needed.'''

# List Example
a_list = [1, 2, 3]
a_list.append(4)
print(a_list)  # Output: [1, 2, 3, 4]

# Dictionary Example
a_dict = {'a': 1, 'b': 2}
a_dict['c'] = 3
print(a_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

'''Immutable data types:
Definition: Immutable data types are those that cannot be modified after their creation.
Examples: Numeric (int, float), String, Tuple.
Characteristics: Elements cannot be changed once set; any operation that appears to modify an immutable object will create a new object.'''


# Numeric Example
a_num = 10
a_num = 20  # Creates a new integer object
print(a_num)  # Output: 20

# String Example
a_str = "hello"
a_str = "world"  # Creates a new string object
print(a_str)  # Output: world

# Tuple Example
a_tuple = (1, 2, 3)
# a_tuple[0] = 4  # This will raise a TypeError
print(a_tuple)  # Output: (1, 2, 3)

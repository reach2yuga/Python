'''1: Iterating over a List'''

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

    '''2: Iterating over a String
A string is also an iterable in Python, meaning you can loop through each character.'''


for i in "Python":
    print(i)


    '''3: Using range() Function
The range() function generates a sequence of numbers, often used with for loops when you need to loop a specific number of times.'''

for i in range(5):
    print(i)

    for i in range(2, 10, 2):  # Start from 2, end before 10, step by 2
     print(i)


     '''4: Iterating Over a Dictionary
You can also iterate over the keys and values of a dictionary.'''


my_dict = {"name": "Alice", "age": 25, "city": "New York"}

for key, value in my_dict.items():
    print(key, ":", value)


    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for num in row:
        print(num, end=" ")
    print()  # Move to the next line after each row

'''break and continue in for Loops
break: Exits the loop when a condition is met.
continue: Skips the current iteration and continues with the next one.'''

for num in range(10):
    if num == 5:
        break  # Exit loop when num is 5
    print(num)


for num in range(5):
    if num == 3:
        continue  # Skip the iteration when num is 3
    print(num)


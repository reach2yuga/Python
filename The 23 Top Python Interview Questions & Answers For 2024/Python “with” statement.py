'''The `with` statement is used for exception handling to make code cleaner and simpler. It is generally used for the management of common resources like creating, editing, and saving a file. 

Example:

Instead of writing multiple lines of open, try, finally, and close, you can create and write a text file using the `with` statement. It is simple.
'''

# using with statement
with open('myfile.txt', 'w') as file:
    file.write('DataCamp Black Friday Sale!!!')
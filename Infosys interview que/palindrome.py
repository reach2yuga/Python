def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

# Test the function
word = "madam"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")


    #string[::-1] uses Python slicing to reverse the string.

#[::-1] means:

#: → take the whole string

#-1 → step backwards (i.e., reverse it)
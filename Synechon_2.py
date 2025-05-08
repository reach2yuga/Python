a = [1, 2, 3, 4, 5]

def reverse_string(a):
    final_list = []  # Initialize an empty list to store the reversed elements
    for i in range(len(a) - 1, -1, -1):  # Loop from the last index to the first index
        final_list.append(a[i])  # Append each element to final_list
    return final_list  # Return the reversed list

# Call the function and print the reversed list
reversed_list = reverse_string(a)
print("Reversed List:", reversed_list)

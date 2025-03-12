# Initialize the previous number
previous_num = 0

print("Printing sum of current and previous number in a range(10):")

# Iterate through the first 10 numbers
for current_num in range(10):
    sum_numbers = previous_num + current_num
    print(f"Current Number: {current_num}, Previous Number: {previous_num}, Sum: {sum_numbers}")
    
    # Update previous number
    previous_num = current_num

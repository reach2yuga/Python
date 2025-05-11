nums = [10, 5, 8, 20, 30]

def find_large_number(numbers):
    large = numbers[0]
    for num in numbers:
        if num > large:
         large = num
    return large
result = find_large_number(nums)
print(result)
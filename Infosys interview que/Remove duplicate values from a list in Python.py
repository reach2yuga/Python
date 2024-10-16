my_list = [1,2,3,2,4,5,3,6,7]
unique_list = set(my_list)
print(unique_list)

unique_list2 = []
for item in my_list:
    if item not in unique_list2:
        unique_list2.append(item)
print(unique_list2)



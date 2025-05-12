list1 = [3,6,7,9,2,3,7,1]
unique_list = []

for i in list1:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)
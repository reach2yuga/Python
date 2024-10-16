arr = [1,4,6,6,8,9,2,5,7]
size = len(arr)
print(size)
i = 0
while i < size-1:
    if arr[i] + arr[i+1] == 10:
        print(arr[i], arr[i+1])
        break
    i = i+1
else:
    print("No element found")
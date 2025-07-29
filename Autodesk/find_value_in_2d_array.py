matrix = [[1, 4, 5],
          [6, 7, 9],
          [10, 11, 20],
          [23, 34, 45]]

target = 9
found =False
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            print(target)
            found = True
            break
    if found:
        break
if not found:
        print(target,"mot found")
    
    
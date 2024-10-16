
a = [1, 2, 3, 2, 4, 5, 1, 6, 3]

def find_duplicates(c):
    duplicates = set()
    b = set()
    for item in c:
     if item in b:
        duplicates.add(item)
     else:
       b.add(item)
    return list(duplicates)
print(find_duplicates(a))
    

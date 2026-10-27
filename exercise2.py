def find_smallest (numbers):
    if not numbers:
        return None

    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
           smallest = n

    return smallest

print(find_smallest([8, 3, 12, 1, 7]))
print(find_smallest([-3, -10, -1, -6]))
print(find_smallest([]))
    

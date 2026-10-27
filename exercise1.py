def find_largest (numbers):
    if not numbers:
        return None

    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n

    return largest

print(find_largest([3, 41, 56, 21, 76, 9]))
print(find_largest([-10, -5, -2, -18]))
print(find_largest([]))            
           

            
def sum7(numbers):
    sum = 0
    i = 0
    double = False
    n = len(numbers)
    if n == 0: return -1
    while i < n:
        sum += numbers[i]
        if double:
            sum += numbers[i]
            double = False
        if numbers[i] == 7: double = True
        i += 1
    return sum

print(sum7([1, 2]))
print(sum7([3, 7]))
print(sum7([7, 5, 6]))
print(sum7([7, 9, 7, 9, 7, 9]))
print(sum7([]))

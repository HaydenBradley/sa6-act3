def find_maximum(numbers, compare_function):

    maximum = numbers[0]

    for num in numbers[1:]:
        maximum = compare_function(maximum, num)

    return maximum

numbers_list = [5, 8, 2, 10, 3, 7]

compare_lambda = lambda x, y: x if x > y else y

result = find_maximum(numbers_list, compare_lambda)

print("The maximum is:", result)

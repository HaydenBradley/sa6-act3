def exponential_list(numbers, n):
    exponential_list = list(map(lambda x: x**n, numbers))
    return exponential_list

numbers_list = [2, 3, 4, 5]
constant_n = 3

result = exponential_list(numbers_list, constant_n)

print(f"List after raising each number to the power of {constant_n}:", result)

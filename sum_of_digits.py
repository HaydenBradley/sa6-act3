sum_of_digits = lambda n: sum(int(digit) for digit in str(n))
number = 12345
result = sum_of_digits(number)
print(f"The sum of digits in {number} is: {result}")
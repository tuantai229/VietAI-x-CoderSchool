# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Answer:
def all_even_digits(num):
    for digit in str(num):
        if int(digit) % 2 != 0:
            return False
    return True

def find_even_digit_numbers():
    result = []
    for num in range(1000, 3001):
        if all_even_digits(num):
            result.append(num)
    return result

output = find_even_digit_numbers()
print(', '.join(map(str,output)))

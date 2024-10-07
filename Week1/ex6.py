# Ex6:  Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Answer:
def find_numbers():
    result = []
    for num in range(2000, 3201):
        if num % 7 == 0 and num % 5 != 0:
            result.append(num)
    return result

output = find_numbers()
print(', '.join(map(str,output)))
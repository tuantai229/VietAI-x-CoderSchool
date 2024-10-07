# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]

# Answer:
n = len(data3)
strongest_neighbour = []

for i in range(n-1):
    if data3[i] > data3[i+1]:
        strongest_neighbour.append(data3[i])
    else:
        strongest_neighbour.append(data3[i+1])

print(f"The strongest neighbour in {data3} is: {strongest_neighbour}")

print(f"The adjacent pair and the strongest neighbour in {data3}:")
for i in range(n-1):
    print(f"({data3[i]},{data3[i+1]}) => {strongest_neighbour[i]}")
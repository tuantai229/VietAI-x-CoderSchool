# Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

# Answer:
frequency = {}
for element in data2:
    if element in frequency.keys(): #check key name element exist in frequecy dictionary
        frequency[element] +=1
    else:
        frequency[element] = 1

frequency_k = []
for key, value in frequency.items():
    if frequency[key] > k:
        frequency_k.append(key)

if len(frequency_k) > 0:
    print(f"The elements in {data2} with frequency is greater than {k} is: {', '.join(map(str, frequency_k))}")
else:
    print(f"There is no element in {data2} with frequency greater than {k}!")
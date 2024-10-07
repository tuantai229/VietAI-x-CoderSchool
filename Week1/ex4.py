# Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]

# Answer:
n = len(data4)

result = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and i != k:
                result.append(int(f"{data4[i]}{data4[j]}{data4[k]}"))

print(f"All possible combinatión from three digits {data4} is: {'; '.join(map(str,result))}")
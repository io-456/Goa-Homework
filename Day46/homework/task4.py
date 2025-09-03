mixed = [2, 5, 8, 11, 14, 17, 20]
even = []
odd = []

for i in mixed:
    if i % 2 == 0:
         even.append(i)
    elif i % 2 != 0:
         odd.append(i)

print(even)
print(odd)              
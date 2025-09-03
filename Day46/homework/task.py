numbers = [1, 4, 7, 10, 13, 16, 19]
new_numbers = []

for i in numbers:
    if i % 2 != 0:
         new_numbers.append(i * 2)    

print(new_numbers)             
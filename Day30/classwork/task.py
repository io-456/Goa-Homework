numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, "ten"]

numbers.remove(1)
numbers.remove(5)
numbers.remove(1)

numbers.pop(0)
numbers.pop(9)
numbers.pop(3)

numbers.append(11)
numbers.append(15)
numbers.append(13)

numbers.insert(9, "name")
numbers.insert(2, 11)
numbers.insert(0, "zero")
print(len(numbers))
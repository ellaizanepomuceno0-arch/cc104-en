numbers = [1, 2, 3, 4, 5, 6]

del numbers[1]
print(len(numbers))
print(numbers)

print(numbers[4])
numbers[4] = 1

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList's length:", len(numbers))  # Printing previous list length.

###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

###


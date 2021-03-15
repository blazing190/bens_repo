

# Get The First Number and Convert To Integer
num1 = int(input("Please Give The Lowest Number: >>> "))

# Get The Second Number and Convert To Integer
num2 = int(input("Please Give The Highest Number: >>> "))

# Get The Sum
sum_of_numbers = num1 + num2

# If Number 1 is less than Number 2 
if (num1 < num2):
    print(num1, num2)
    print("Total", sum_of_numbers)

# If Number 1 is equal to Number 2
elif (num1 == num2):
    print(num1, num2)
    print("Total", sum_of_numbers)
    print("Both Numbers Are Equal Btw")

# If number 1 is more than number 2 flip order, and tell the user about the error
else:
    print(num2, num1)
    print("Total", sum_of_numbers)
    print("Please Make Sure To Follow The Prompt And Give Number 1 As The Lowest Number Followed By Number 2 Which Is Larger / Equal To Number 1")

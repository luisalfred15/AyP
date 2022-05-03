print("**** Welcome to the calculator ****")
is_valid_operation = True

option = input("Please select one option: \n1- Sum\n2- Substraction \n3- Multiply \n4- Division\n -->")

if option.isnumeric():
    option = int(option)
else:
    print("Invalid number")
    is_valid_operation = False

number_one = input("Please enter the first number\n -->")
number_two = input("Please enter the second number\n -->")

if number_one.isnumeric():
    number_one = int(number_one)
else:
    print("Invalid number")
    is_valid_operation = False

if number_two.isnumeric():
    number_two = int(number_two)
else:
    print("Invalid number")
    is_valid_operation = False

if is_valid_operation: 
    if option == 1:
        result = number_one + number_two
        print("The result is:", result)
    elif option == 2:
        result = number_one - number_two
        print("The result is:", result)
    elif option == 3:
        result = number_one * number_two
        print("The result is:", result)
    elif option == 4:
        if number_two != 0:
            result = number_one / number_two
            print("The result is:", result)
        else:
            print("The second can not be zero")
        
    else:
        print("Invalid option")
else:
    print("Invalid Operation")
#Calculator

def calculator(command):
    if command == "addation":
        def addation(number_1,number_2):
            total_addation = number_1 + number_2
            return total_addation
        input_number_1 = int(input("Please enter first number:\n"))
        input_number_2 = int(input("Please enter second number:\n"))
        result = addation(input_number_1,input_number_2)
        print(f"The result of {command} is : {result}")

    elif command == "subtraction":
        def subtraction(number_1,number_2):
            total_subtraction = number_1 - number_2
            return total_subtraction
        input_number_1 = int(input("Please enter first number:\n"))
        input_number_2 = int(input("Please enter second number:\n"))
        result = subtraction(input_number_1,input_number_2)
        print(f"The result of {command} is : {result}")

    elif command == "multiplication":
        def multiplication(number_1,number_2):
            total_multiplication = number_1 * number_2
            return total_multiplication
        input_number_1 = int(input("Please enter first number:\n"))
        input_number_2 = int(input("Please enter second number:\n"))
        result = multiplication(input_number_1,input_number_2)
        print(f"The result of {command} is : {result}")

    elif command == "division":
        def division(number_1,number_2):
            total_division = number_1 / number_2
            return total_division
        input_number_1 = int(input("Please enter first number:\n"))
        input_number_2 = int(input("Please enter second number:\n"))
        result = division(input_number_1,input_number_2)
        print(f"The result of {command} is : {result}")

input_command = input("What is your request?\n ")
total_result = calculator(input_command)

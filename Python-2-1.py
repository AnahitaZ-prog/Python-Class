#Mini- Calculator

first_number = int(input("Enter a number:\n"))
second_number = int(input("Enter another number:\n"))
result=""
oprator = input("What do you want me to do?\n")

if oprator == "+":
    result = first_number + second_number

elif oprator == "-":
    result = first_number - second_number

elif  oprator == "*":
    result = first_number * second_number

elif oprator == "/":
    result = first_number / second_number

elif oprator == "**":
    result = first_number ** second_number

else:
    result="Youre demand is Invalid!."

print("The result is:\t", result)

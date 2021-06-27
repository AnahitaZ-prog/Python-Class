#Print 1 to n and print that's cool when numbers are divisible to 2,4,6,9.
n = int(input("Please enter a number:\n"))
number = 1
while number <= n:
    print(number)
    if number % 2 == 0:
        print("That's cool!.")
    elif number % 4 == 0:
        print("That's cool!.")
    elif number % 6 == 0:
        print("That's cool!.")
    elif number % 9 == 0:
        print("That's cool!.")
    number += 1

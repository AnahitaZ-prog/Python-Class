#Assisstance of a students for calculating side and circumference
import math

while True:
    def  rectangle(length,width,command):
        if command =="side":
            side = length * width
            total_side = side
            return total_side
        elif command == "circumference":
            circumference = 2 * (length + width)
            total_circumference = circumference
            return total_circumference

    def circle(command,radius, diameter):
        if command == "side":
            side = math.pi * radius * radius
            total_side = side
            return total_side
        elif command == "circumference":
            circumference = math.pi * diameter
            total_circumference =  circumference
            return total_circumference

    def triangle(base,height,command):
        if command == "side":
            side = (base * height) / 2
            total_side = side
            return total_side
        elif command == "circumference":
            circumference = base * 3
            total_circumference =  circumference
            return total_circumference


    shape = input("What shape do you want?\n")

    if shape == "rectangle":
        input_command = input("What is your request?\n")
        input_length = int(input("Please enter a length:\n"))
        input_width = int(input("Please enter a width:\n"))
        result = rectangle(input_length,input_width,input_command)
        print(f"{input_command} of rectangle is : {result}")

    elif shape == "circle":
        input_command = input("What is your request?\n")
        input_radius = int(input("Please enter a radius:\n"))
        input_diameter = int(input("Please enter a diameter:\n"))
        result = circle(input_command,input_radius,input_diameter)
        print(f"{input_command} of circle is : {result}")

    elif shape == "triangle":
        input_command = input("What is your request?\n")
        input_base = int(input("Please enter a base:\n"))
        input_height = int(input("Please enter a height:\n"))
        result = triangle(input_base,input_height,input_command)
        print(f"{input_command} of triangle is : {result}")

    command = input("Do you want to continue?\n")
    if command == "yes":
        continue
    elif command == "no":
        print("bye")
        break

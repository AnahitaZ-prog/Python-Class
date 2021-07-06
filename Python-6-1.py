#Delete duplicate name

numbers = [1,2,3,14,25,80,25,18,20,55,80,100]
numbers = list(dict.fromkeys(numbers))
print(numbers)           

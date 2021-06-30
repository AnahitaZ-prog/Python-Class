# print divisible number to n

n=0
number = int(input("Please enter a number:\n"))
print("\n\n")

while n <= 20:
    #print(n)
    if n % number == 0:
        print(n)
    n += 1

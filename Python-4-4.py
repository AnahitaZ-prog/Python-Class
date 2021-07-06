#Hop Game

number = 0
hop = []
while number <= 6:
    # replay = input("Do you want to start?\n")
    # if replay == "yes":
    #     number = int(input("Enter a number,please:\n"))
    # else:
    #     print(1)
    number = int(input("Enter a number,please:\n"))
    hop.append(number)
    number += 1

    for i in range(len(hop)):
        for j in range(i+1,len(hop)):
            if hop[i] == hop[j]:
                print("GAME OVER!.")
            break

    while number % 5 == 0:
        if number == 'hop':
            continue
        else:
            print("GAME OVER!.")
            break


    #hop.append(number)
        #compare(hop[i],hop[j])

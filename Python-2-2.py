#BMI

Primary_weight = input("Please Enter you're weight.\n")
Primary_height = input("Please Enter you're height.\n")
weight = int(Primary_weight)
height = int(Primary_height)
height_calc = (height/100)**2
BMI = weight/height_calc
#print(BMI)
if BMI < 25:
    print(BMI,"\n You are healthy.")
elif BMI >= 25 and BMI <= 29.9:
    print(BMI, "\n You are overweight.")
elif BMI >= 30 and BMI < 40:
    print(BMI, "\n You are Fat.")
else:
    print(BMI, "\n You are in DANGER!.")         

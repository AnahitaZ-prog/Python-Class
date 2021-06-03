Primary_weight = input("Please Enter you're weight.\n")
Primary_height = input("Please Enter you're height.\n")
weight = int(Primary_weight)
height = int(Primary_height)
def BMI ():
    height_calc = (height/100)**2
    BMI = weight/height_calc
    print(BMI)
#BMI()

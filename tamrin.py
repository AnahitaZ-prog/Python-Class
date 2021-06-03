
def mostatil(tool , arz , command):
    if command == "mohit":
        mohit = 2*(tool+arz)
        print("mohit:\t" , mohit)
    if command == "masahat":
        masahat = tool * arz
        print("masahat:\t", masahat)
vorodi_1 = int(input("tool adad vared konid;\n"))
vorodi_2 = int(input("arz adad vared konid;\n"))
vorodi_3 = input("Command ra vared konid:\n")
mostatil(vorodi_1 , vorodi_2 , vorodi_3)


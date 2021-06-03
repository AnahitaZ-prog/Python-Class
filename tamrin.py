def mostatil(tool , arz , command):
     if command == "mohit":
         mohit = 2*(tool+arz)
         result= mohit
     if command == "masahat":
         masahat = tool * arz
         result= masahat
     return result

vorodi_1 = int(input("tool adad vared konid;\n"))
vorodi_2 = int(input("arz adad vared konid;\n"))
vorodi_3 = input("Command ra vared konid:\n")
result = mostatil(vorodi_1 , vorodi_2 , vorodi_3)
print(result)
mostatil(vorodi_1 , vorodi_2 , vorodi_3) 



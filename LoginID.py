##################################################################

#LOGIN


a = "Introduzca su ID \n"
#f = 
b = 702790071
while a:
  c = input(a)
  
  if int(c) == b:
    print("el ID de", len(c), "digitos es correcto")
    break
  
  elif int(c) > b:
      print("el ID es incorrecto, tiene", len(c), "digitos, tiene digitos de mas")

  elif int(c) < b:
      print("el ID es incorrecto, tiene", len(c), "digitos, faltan digitos")
        
##################################################################

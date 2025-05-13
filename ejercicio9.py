year = int(input("ingrese un año"))
#use un if anidado pero debi usar el elif
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(" el año es bisiesto")
        else:
         print("el año no es bisiesto")
    else:
       print("el año es bisiesto")
else: 
   print("el año no es bisiesto")

 
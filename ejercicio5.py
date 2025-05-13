cuenta = float(input("¿cual es el total de la cuenta"))

print("¿Que valor deseas dejar de propina?")
print("1) 10%")
print("2) 15%")
print("3) 20%")

propina = input ("elegir propina") # se tiene que crear la variable de propina para poder realizar operaciones

if propina=="1":
    cuentatotal = cuenta*0.10
    print("total",cuentatotal)

elif propina=="2":
    cuentatotal = cuenta*0.15
    print("total",cuentatotal)

elif propina=="3":
    cuentatotal = cuenta*0.30
    print("total", cuentatotal)

else:
    print("Opcion no valida")


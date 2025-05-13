peso = float(input("Ingrese su peso"))
altura = float(input("Ingrese su altura"))

imc = (peso / altura ) *2

if imc < 18.5:
    print("Bajo peso")
elif imc >= 18.5 and imc <=29.9:
    print("Normal")
elif imc >= 25 and imc <=29.9:
    print("Sobrepeso")
elif imc >= 30:
    print("Obesidad")








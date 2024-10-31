print("########## exercise 1 #########")

number1 = float(input("Ingrese el primer número: "))
number2 = float(input("Ingrese el segundo número: "))

suma = number1 + number2
resta = number1 - number2
multiplicacion = number1 * number2
division = number1 / number2
porcentaje = number1 % number2
potencia = number1 ** number2

print("Suma",{suma})
print("Resta", {resta})
print("División", {division})
2

print("Porcentaje", {porcentaje})
print("Potencia", {potencia})

print("########## exercise 2 #########")

age = int(input("Ingrese su edad: "))
country = input("Ingrese su país: ")

if age >= 18 and country.lower() == "españa":
    print("La persona puede voter en las elecciones")
else:
    print("La persona no puede votar en la elecciones")

print("########## exercise 3 #########")

userNum1 = float(input("Ingrese el primer número: "))
userNum2 = float(input("Ingrese el segundo número: "))
userNum3 = float(input("Ingrese el tercer número: "))

numberList = [userNum1,userNum2,userNum3]

mayor = max(numberList)
menor = min(numberList)

print(f'El número mayor es :', {mayor})
print(f'El número menor es: ', {menor})

print("########## exercise 4 #########")

precioIni = float(input("Ingresa el valor original del producto: "))
porcentajeDes = float(input("Ingrese el decuento del producto: "))

descuento = precioIni * (porcentajeDes/100)

precioFinDes = precioIni - descuento

print("El precio final del producto con su decuentos es: ",{precioFinDes})

print("########## exercise 5 #########")

año = int(input("Ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
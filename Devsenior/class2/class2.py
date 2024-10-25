var1 = 100
var2 = 200
var = var1 + var2
#print = ("Var: ",var)

ancho = 1023
alto = 1000
area = ancho * alto
#print = ("Area: ",area)

a = 10
b = 3
c = a/b
#print ("C: ",c)

altura = 80
peso = "80"

# "80"
pesoNumEnt = int(peso)

# "80.0"
pesoNumFloat = float(peso)

peso2 = str(pesoNumEnt)

# "80" == "80.0"
#print(peso == peso2)

# "80" == "80.0"
#print (pesoNumEnt ==pesoNumFloat)


# Ejercicio 1

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

inputUsuario= input("Ingre el primero número :")

isFloat = is_float(inputUsuario)


# if logic operation:
#   action
if not isFloat :
        inputUsuario = input("El número no es valido, ingrese de nuevo el primer número: ")

numero1 = float (inputUsuario)

numero2 = float(input("Ingreso el segundo número :"))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print("Suma :", suma)
print(f"Suma:,{suma}")
print(f"Resta:",{resta})
print(f"Multiplicación:,{multiplicacion}")
print(f"División:,{division}")


print("########## exercise 1 #########")

import random

# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)
adivinado = False

while not adivinado:
    adivinanza = int(input("Adivina el número (entre 1 y 10): "))
    if adivinanza == numero_secreto:
        print("¡Felicidades! Has adivinado el número 🎉")
        adivinado = True
    elif adivinanza < numero_secreto:
        print("El número es mayor 📈")
    else:
        print("El número es menor 📉")

print("########## exercise 2 #########")

while True:
    calification = float(input("Ingrese su calificació entre 0 y 100: "))



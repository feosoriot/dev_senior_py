print ('######## Listas ########')
nombres = ['Juan', 'Sebastian', 'Melissa', 'Xiomara']

print (nombres)
print(nombres[1])
#Saber el ultimo dato agregado -1
print(nombres[-1])
print(nombres[0:2])
# Para conocer la cantidad de elementos de la lista
print("\nPara conocer la cantidad de elementos de la lista")
print(len(nombres))
# Para adicionar un elemento al final de la lista
print("\nPara adicionar un elemento al final de la lista")
nombres.append("Elizabeth")
print(nombres)
# Para insertar un elemento en una posición específica
print("\nInserto a María en la segunda posición de la lista")
nombres.insert(1, "María")  # Inserto a María en la segunda posición de la lista
print(nombres)
# Para eliminar un elemento de la lista
print("\nElimina el elemento especificado")
nombres.remove("Elizabeth")  # Elimina el elemento especificado
print(nombres)
print("\nElimina el último elemento de la lista")
nombres.pop()  # Elimina el último elemento de la lista
print(nombres)
print("\nElimina según el índice especificado")
del nombres[1]  # Elimina según el índice especificado
print(nombres)
nombres.pop(1)  # Elimina según el índice especificado
print(nombres)
nombres.clear() # Limpiar la lista
print(nombres)
#del nombres # Eliminar lista con su estructura
#print(nombres)
print('\n')
print ('######## Tuplas ########')

paises = ('Colombia', 'Mexico', 'Ecuador', 'Venezuela')
print('\n')
print(paises)
print(len(paises))
print(paises[2])
print(paises[-1])
for pais in paises:
    print(pais)

# convertir una tupla-->lista y lista-->tupla
paisesLista = list(paises)
paisesLista [1] = 'Argentina'
paises = tuple(paisesLista)
print(paises)

#del paises
#print(paises)

print('\n')
print ('######## Set ########')
lenguajes = {'Java', 'Python', 'JavaScrip'}

print(lenguajes)
print(len(lenguajes))
print('Go' in lenguajes)
print('Java' in lenguajes)
lenguajes.add('Go')
print(lenguajes)
for lenguaje in lenguajes:
    print(lenguaje)
lenguajes.remove('Java')
print(lenguajes)
lenguajes.discard('Python')
print(lenguajes)


print('\n')
print ('######## Diccionario ########')

conceptosProgramacion = {
    'POO': 'Programacion Orientada a Objetos',
    'IDE': 'Entorno de Desarrollo Integrado',
    'DBMS': 'Sistema de Gestion de Base de Datos'  
}

print(conceptosProgramacion)
print(len(conceptosProgramacion))

print(conceptosProgramacion['IDE'])
print(conceptosProgramacion.get('POO'))

conceptosProgramacion ['DBMS'] = 'Database Manangment System'
print(conceptosProgramacion['DBMS'])

for key in conceptosProgramacion:
    print(key)

for key, value in conceptosProgramacion.items():
    print(key, value)

    
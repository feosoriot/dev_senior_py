#Importar libreria para fechas--> datetime
from datetime import datetime
import statistics

class Tarea:
    #funcion de inicialazion = metodo constructor
    def __init__(self, nombre, fechaLimite, categorias, horasDedicadas):
        self.nombre = nombre
        self.fechaLimite = fechaLimite
        self.categorias = categorias
        self.horasDedicadas = horasDedicadas

#funcion para agregar una tarea
def agregarTarea(listaTareas):
    nombre = input('Ingrese el  nombre de la tarea: ')
    fechaLimite_str = input('Ingrese la fecha limite de la tarea (DD/MM/YYYY): ')
    try:
        fechaLimite = datetime.strptime(fechaLimite_str, "%d/%m/%Y") 
    except ValueError: 
        print('Fecha no valida')
        return
    categorias = ('Ingrese la categoria (Estuido, Trabajo, Personal, Otras): ')
    horasDedicadas_str = input('Ingrese las horas dedicadas, separadas en coma ej 3,5,6: ')
    try:
        horasDedicadas = list(map(float, horasDedicadas_str.split(",")))
    except ValueError:
        print("Horas no validas")
        return
    
    #crear un objeto y lo agrega, para encapsular en un objeto las tareas   
    tarea = Tarea (nombre, fechaLimite, categorias, horasDedicadas)
    listaTareas.append(tarea)
    print('Tarea agregada con exito...')

def visualizarTareas(listaTareas):
    if not listaTareas:
        print('No hay tareas registradas')
        return
    
    for i, tarea in enumerate(listaTareas, start= 1):
        print(f'\nTarea {i}')
        print(f'nombre : {tarea.nombre}')
        print(f'Fecha limite : {tarea.fechaLimite.strftime("%d/%m/%Y")}')
        print(f'Categoria : {tarea.categotias}')
        print(f'Horas decicadas : {tarea.horasDedicadas}')

def analizarHoras(listaTareas):   
    if not listaTareas:
        print('No hay tareas registradas')
        return
    
    for tarea in listaTareas:
        promedio = statistics.mean(tarea.horasDedicadas)
        maximo =max(tarea.horasDedicadas)
        minimo = min(tarea.horasDedicadas)
        print(f'\nAnalisis {tarea.nombre}')    
        print(f'Promedio de horas : {promedio}')    
        print(f'Maximo de horas: {maximo}')    
        print(f'Minimo de horas: {minimo}')

def generarInforme(listaTareas):
    if not listaTareas:
        print('No hay tareas registradas')
        return

    #abri un archivo txt para escribir un informe
    with open("Informe_tareas.txt","w") as archivo:
        #Escribir los detalles de la tarea en el archivo
        for tarea in listaTareas:
            archivo.write(f"Nombre : {tarea.nombre}\n")
            archivo.write(f'Fecha limite : {tarea.fechaLimite.strftime("%d/%m/%Y")}\n')
            archivo.write(f'Categoria : {tarea.categotias}\n')
            archivo.write(f'Horas decicadas : {tarea.horasDedicadas}\n')
            archivo.write("\n")
    print("Informe generado como 'informe_tarea.txt': ")


def menu():
    listaTareas = []
    while True:
        print("\nMenu de opciones: ")
        print("1. Agregar tarea: ")
        print("2. Visualizar tareas: ")
        print("3. Analizar horas dedicadas: ")
        print("4. Generar informe: ")
        print("5. Salir : ")

        opcion = input("Seleccione una opcion:")

        if opcion == "1":
            agregarTarea(listaTareas)
        elif opcion == "2":
            visualizarTareas(listaTareas)
        elif opcion == "3":
            analizarHoras(listaTareas)
        elif opcion == "4":
            generarInforme(listaTareas)
        elif opcion == "5":
            print("saliendo del programa...")
            break
        else:
            print("opcion invalida")
            

if __name__ == "__main__":
    menu()        



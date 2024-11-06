#codificacion camel case
#Si es un numero que tiene decimales es float
#si es entero es int
#Si es texto String

ventasTotales = 0.0

#solicitar el numero de productos
numProductos = int(input('Ingrese el numero de procutos a gestionar: '))

#listas para almacenar la informacion
# [] para listas

nombres = []
precios = []
cantidades = []

print ('Ingreso inicial de productos a la tienda: ')


for i in range(numProductos):
    print(f'Producto {i+1}: ')
    nombre = input('Ingrese el nombre del producto: ').lower()
    nombres.append(nombre)
    precio = float(input('Digite el precio del producto: '))
    precios.append(precio)
    cantidad = int(input('Ingrese la cantidad del producto: '))
    cantidades.append(cantidad)

#ciclo principal del menu
while True:
    print('\n --MENU DE GETION DE DROGREIA--')
    print('1. Vender producto')
    print('2. Mostrar Inventario')
    print('3. Mostrar Ventas Totales')
    print('4. Salir')

    opcion = int(input('Ingrese una opcion: '))

    if opcion == 1:
        print('\nVender Producto')
        nombreVenta = input('Ingrese el nombre del producto a vender : ').lower()
        cantidadVender = int(input('Ingrese la cantidad a vender : '))
        productoEncontrado = False

        for i in range(len(nombres)):
            if nombres[i] == nombreVenta:
                productoEncontrado = True
                if cantidadVender <= cantidades[i]:
                    totalVenta= cantidadVender * precios [i]
                    ventasTotales += totalVenta
                    cantidades [i] -= cantidadVender
                    print(f'Venta realizada. total de esta venta $ {totalVenta:.2f}')
                    print(f'Queda {cantidades[i]} unidades de {nombres [i]} en el inventario')
                else:
                    print(f'cantidad insuficiente de inventario. ya que en stock solo tenemos {cantidades[i]}')
                break

        if not productoEncontrado:
            print('Producto no encontrado en el interio')

    elif opcion == 2:
        print('\nInvetario de productos')
        for i in range(len(nombres)):
            print(f'Producto {i+1}: {nombres[i].capitalize()}, Precio: ${precios[i]:.2f}, Cantidad: {cantidades[i]}') 

    elif opcion == 3:
        print(f'\nVentas totales acumuladas: ${ventasTotales:.2f}')

    elif opcion == 4:
        print('Gracias por usar el sistema de gestion droguera devSenior')
        break

    else:
        print('Opcion invalida. ingresar entre (1-4)')
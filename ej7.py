'''
nombre: Hadassa Galindo
Fecha: 3 de febrero 2025
descripción del ejercicio:
Encontrar el índice de un elemento con index()
Crea una lista con varios colores, por ejemplo ["rojo", "azul", "verde", "amarillo", "negro"].

Pide al usuario que ingrese un color.

Usa un

try/except
para manejar posibles errores:

Dentro del try, usa index() para obtener la posición del color ingresado.
Muestra la posición en pantalla.
En el except, muestra un mensaje indicando que el color no está en la lista.
'''
colores=["rojo", "azul", "verde", "amarillo", "negro"]
while True:
    x=input('ingrese el nombre de un color: ')
    if x in colores:
        print(f'este color esta en la posicion: {colores.index(x)+1}')
        break
    else:
        print(f'{x} no esta en los colores ingresados')
        continue
        

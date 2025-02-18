'''
nombre: Hadassa Galindo
Fecha: 3 de febrero 2025
descripción del ejercicio:
Creación y manipulación básica de listas
Crea una lista vacía llamada frutas.
Pide al usuario que ingrese 3 frutas y añádelas a la lista usando append().
Muestra la lista resultante.
Crea una función definida por el usuario que reciba una lista y la imprima en pantalla.
Llama a la función pasando la lista frutas.
'''

import os
frutas=[]
def vali(msg):
    while True:
        x=input(msg)
        if x.isalpha():
            break
        else:
            print('dato no valido . . .')
    return x
def mostrar(frutas):
    os.system('cls')
    for i in frutas:
        print(i)
print('---------BIENVENIDO---------')
frutas.append(vali('ingrese el nombre de la 1ra fruta: '))
frutas.append(vali('ingrese el nombre de la 2ra fruta: '))
frutas.append(vali('ingrese el nombre de la 3ra fruta: '))
print(frutas)
mostrar(frutas)
print('----------------------------')
 
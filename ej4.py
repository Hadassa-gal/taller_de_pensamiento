'''
nombre: Hadassa Galindo
Fecha: 3 de febrero 2025
descripción del ejercicio:
Eliminando elementos de una lista
Crea una lista llamada animales con valores a tu elección (ej. ["perro", "gato", "elefante", "tigre"]).
Pide al usuario un nombre de animal para eliminar de la lista.
Antes de eliminar, utiliza una estructura if para verificar si el animal está en la lista.
    Si está, usa remove() para quitarlo.
    Si no está, muestra un mensaje indicando que no se encontró.
'''

animales=['perro','gato','elefante','tigre']
print(animales)
while True:
    x=input('ingrese el nombre del animal que quiera eliminar: ')
    if x in animales:
        animales.remove(x)
        print(animales)
        break
    else:
        continue

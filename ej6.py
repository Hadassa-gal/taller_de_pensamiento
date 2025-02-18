'''
nombre: Hadassa Galindo
Fecha: 3 de febrero 2025
descripción del ejercicio:
Limpiando una lista con clear()
Crea una lista con al menos 5 elementos a tu elección.
Define una función llamada limpiar_lista que reciba una lista y la vacíe usando clear().
Antes de llamar a la función, muestra la lista original.
Llama a la función y luego imprime la lista para confirmar que está vacía.
'''
lista=['perro',3,'gato',1,'nose',10]
def limpiar_lista(x):
    x.clear()
    return x
print(lista)
limpiar_lista(lista)
print('--------------------')
print(lista)
'''
nombre: Hadassa Galindo
Fecha: 3 de febrero 2025
descripción del ejercicio:
Función para mostrar contactos con filtro
Partiendo de la agenda del ejercicio anterior, crea una función llamada mostrar_contactos que reciba la lista de contactos y un filtro (una cadena) para el nombre.
La función recorre la lista de contactos (usando un ciclo for):
Si el nombre del contacto contiene la cadena del filtro (usa funciones de cadena como in, lower()), imprime los datos del contacto.
Prueba la función solicitando al usuario un filtro.
'''
def mostrar_contactos(lista):
    for key,valor in lista:
        print(f'{key}:{valor}')
lista={}
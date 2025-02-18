'''
nombre: Hadassa Galindo
Fecha: 3 de febrero 2025
descripción del ejercicio:
Insertar elementos en posiciones específicas
Crea una lista llamada lenguajes que contenga ["Python", "C", "Java"].
Pide al usuario un nuevo lenguaje de programación.
Usa insert() para colocar el nuevo lenguaje en la posición 1 de la lista.
Muestra el resultado final.
'''
lenguaje=['python','c','java']
print(lenguaje)
lenguaje.insert(0,input('ingrese un nuevo lenguaje: '))
print(lenguaje)
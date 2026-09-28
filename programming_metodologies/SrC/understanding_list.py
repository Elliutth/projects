"""
las listas nos permite almacenar informacion en un lugar
 la cantidad que se desee: ya sean pocos elementos
 o millones de elementos.

 una lista es una coleccion de items (elementos) que tiene
 un orden particular. se pueden crear listas que incluyan 
 strings, enteros, floats, los nombres de las personas de tu
 familia, etcetera, podemos almacenar (los tipos de datos
 permitidos en python) lo que queremis en una lista.

 son elementos mutables: puede modificarse el tamaño de la lista.

 se recomienda nombrar una variable del tipo lista en plural

 en python, los corchetes [] indican una lista, 
 sus elementos se separan por comas

 ejemplo:
"""
bicycles = ["trek", "cannondale", "redline", "specialized", "apache"]
print(bicycles)

# ¿como podemos acceder a los elementos de una lista?

"""
las listas son colecciones ordenadas. se puede acceder
a un elemento de una lista diciendole a python la posicion
o indise del elemento deseado.

para obtener el valor deseado, se debe escribir
el nombre de la lista, seguido del indice del elemento
entre corchetes.
"""
print(bicycles[2])
print(bicycles[0],bicycles[1],bicycles[2])

print(bicycles[0].upper())

# los indices comienzan en 0, no en 1
#ejemplo
print(bicycles[1]) #cannondale
print(bicycles[3]) #specialized

#accediendo al ultimo elemento de una lista
print(bicycles[-1])
print(bicycles[-2])

#utilizando valores individuales de una lista
message = f"My first bicycle was a {bicycles[-1].upper()}"
print(message)
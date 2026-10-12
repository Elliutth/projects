"""

TUPLAS

las tuplas son listas de elementos que no cambias de tamaño
las tuplas son listas inmutables

se utilizan parentesis () para definir una tupla

ejemplo 

si tenemos un rectangulo (largo, ancho) que siempre va
a tener cierto tamaño podemos asegurar que sus dimenciones
no va a cambiar si colocamos sus valores en una tupla

"""

dimensions = (200, 50) # 200 de largo por 50 de ancho
print(dimensions)

#vanos a imprimir elementos de una tupla
#se realiza de la misma forma que con una lista
print(dimensions[0])
print(dimensions[1])
print(dir(dimensions))

#vamos a modificar el valor de una lista
names = ["carlos", "charly", "juan", "wendy"]
print(names)
names[0] = "mercury" 
names[1] = "mercury" 
names[2] = "mercury" 
print(names)


#dimensions[0] = 500 #Esta operacion no esta permitida

#looping through a tuple
for dimension in dimensions:
    print(dimension)
"""
no podemos modificar una tupla, 
lo que si podemos hacer es cambiar
la asignacion de una variable que
almacena una tupla
"""
dimensions = (500, 1000, 20)
print("tupla reasignada", dimensions)

#lisa 
#dimensions_2 = (200, 50)
#print(dir(dimensions_2))

# string
#name = "charly"
#print(dir(name))

#
#age = 34
#print(dir(age))

# tipos de datos booleanos
answer = True
print(answer)
#print(dir(answer))
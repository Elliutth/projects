# Listas de numeros
"""
las listas tambien pueden almacenar numeros. python 
ofrece varias herramientas que ayudan a trabajar 
eficientemente con listas de numeros
"""
# metodo build-in range()
"""
el metodo range() nos ayuda a crear facilmente series de numeros
ejemplo
"""
for value in range(1,5):
    print(value)
#range es un intervalo abierto por la izquierda y cerrado por la derecha





#crea una lista de numeros utilizando range
numbers = list(range(0,10))
print(numbers)

# lista de numeros pares
even_numbers = list(range(0,11,2))
#que pasa con un paso negativo?
print(even_numbers)

#build in print() sorted() type() len() str() list() range()
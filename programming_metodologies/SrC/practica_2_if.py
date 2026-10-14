"""
ejercicio
realizar un programa que determine el costo de 
un boleto a partir de las siguientes condiciones

-costo para una persona igual o menot a 4 años : gratis
-costo para una persona cuya edad es mayor a 4 años pero 
  menor o igual a 18: 200
-costo para una persona cuya edad es mayor a 18: 500
"""
age = input("ingresa tu edad: ")
#print(type(age)) # string
age = int(age)
#print(type(age))# entero int
if age <= 4:
    cost = 0

if age > 4 and age <= 18:
    cost =200

if age > 18:
    cost = 500

print(f"el caso de tu boleto es: {cost}")

#if- elif- else
print("\n esto se realiza con el bloque if-elif-else")

if age <= 4:
    cost = 0
elif age > 4 and age < 18:
    cost =200
elif age >= 18 and age < 65:
    cost = 500
elif age >= 65:
    cost = 0
#else: 
 #   cost = 0

print(f"el caso de tu boleto es: {cost}")

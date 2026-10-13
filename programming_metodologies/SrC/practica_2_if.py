"""
ejercicio
realizar un programa que determine el costo de 
un boleto a partir de las siguientes condiciones

-costo para una persona igual o menot a 4 años : gratis
-costo para una persona cuya edad es mayor a 4 años pero 
  menor o igual a 18: 200
-costo para una persona cuya edad es mayor a 18: 500
"""
age = 18
if age <= 4:
    cost = 0

if age > 4 and age <= 18:
    cost =200

if age > 18:
    cost = 500

print(f"el caso de tu boleto es: {cost}")

#if- elif- else
#numeros
#enteros - integers

""" 
los numeros enteros los podemos 
sumar (+), restar (-), multiplicar(*), dividir(/)
"""
print(2+3)
print(3-2)
print(2*3)
print(3/2)
number_1 = 5
number_2 = 10
print(number_1 + number_2)

## dividir /
## divicion entera
# potencia **n

print(3**2) #3^2
print(3**3) #3^3
print(10**6)#10^6
print(10%2) #residuo de divicion (modulo (mod))

age = 18
print(age)
name = "elliutth isaac"
print(name, age)

# floats
"""
python llama floats a cualquier numero
 con punto decimal
"""
print(0.1 + 0.1)
print(0.2 - 0.2)
print(2*0.1)
print(2*0.2)

#imprimir la edad de alguine
age = 34 # variable del tipo int
# message = "charly tiene" + age + "años."
message = "charly tiene " str(age) " años"
message_f = f"charly tiene {age} años."
print(message)
print(message_f)
"""
typeError: python no puede reconoser el tipo
de informacion que se esta utilizando

en este caso no se puede concatenar int a string
"""
print(type(age))
print(type(0.1))
print(type(message_f), type(5+1))

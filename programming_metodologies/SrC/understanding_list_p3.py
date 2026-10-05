# trabajando con listas

print("\n\tlas listas estan chidas y sigo aprendiendo de ellas".upper())
magicians = ["harry", "ron", "hermione", "snape"]
print (magicians)

print (magicians [0],magicians [1], magicians [2], magicians [3])

# Ciclo for
for magician in magicians:
    print(magician) 

# A esto se le conoce como looping
# for cat in cats:
# for dog in dogs:
# for item in items: 
# Ahora vamos a imprimir un mensaje para cada mago
for magician in magicians:
    print(f"{magician.title()} ese fue un gran hechizo. ")
    print(f"no puedo esperar a ver el siguiente hechizo, {magician.upper()}")
print("gracias a todos. fue un gran espectaculo")

# Identacion
"""
python utiliza la identacion para identificar cuando
una linea de codigo esta conectada a la linea de codigo
anterior

basicamente, se utiliza 4 espacios en blanco para
obligarnos a escribir codigo ordenado y estructurado
"""
#No olvidemos identar
magicians = ["alice", "david", "caroline"] 
#for magician in magicians
#print(magician) identation error

#error de logica - logic error - identation error
for magician in magicians:
    print(magician) 
print(f"no puedo esperar a ver el siguiente truco, {magician}")

# Evitar identacion inmecesaria
message = "hello python world!"
#    print(message)

# No olvidar los dos puntos - sintax error
# for magician in magicians
#    print(magician)
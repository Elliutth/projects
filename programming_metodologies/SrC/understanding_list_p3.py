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
players = ["charly", "juan", "iancarlo", "lisamdro"] 
print("lista original:", players)
#slicing

print(players[0:2]) #charly juan

#el slicing me permite tranajar con un grupo
#especifico de una lista: al resultado se le conoce como
#"un slice"

print("1:4", players[1:4]) # juan iancarlo lisandro
print(":3", players[:3])#charly juan iancarlo
print("2:", players[2:]) #iancarlo lisandro
print("[-3:]",players[0:2]) #juan iancarlo lisandro

#players = ["charly", "juan", "iancarlo", "lisamdro"] 
#casos especiales
print(players[1:6]) # juan iancarlo lisandro
print(players[6:1]) # lista vacia
print(players[:0]) #lista vacia

# looping through a slice
print("looping trhough a slice")
students = ["charly", "juan", "iancarlo", "lisamdro"] 
for student in students[2:4]:
    print(f"el estudiante {student} , va a pasar la materia")
print(students)

#¿como podemos copiar una lista?
my_food = ["pizza", "tacos", "flautas"]
my_friend_food = my_food #manera erronea de copiar una lista

#tres maneras de copiar una lista
# metodo 1 - utilizando slicing
my_friend_food_2 = my_food[:]
#metodo 2 - utilizando el metodo copy
my_friend_food_3 = my_food.copy()
#metodo 3 utilizando el metodo list
my_friend_food_4 = list(my_food)

# tipos de daros (python)
#strings - "" .title .upper .lower .lstrip .rstrip .strip .join
#concatenacion - nativo(+) f-strings .join()
#tipos de datos numericos - operaciones - jerarquia de operaciones
#enteros - int
# floats - flotantes 
# listas - [] - como acceder a elementos de una lista [i]
#metodos - .pop .sort . reverse .remove .append .insert .copy
#looping - for
# slicing
#build-in .print .sorted .type .len .range .list .str
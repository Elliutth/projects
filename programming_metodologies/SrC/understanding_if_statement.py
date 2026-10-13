#if statement
cars =["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car)


#el condicional o condition
# El condicional es el corazon del if

# condicional verdadero
# condicional true
truck = "ford"
print(truck == "ford")

# condicional falso 
#conditional false
print(truck == "audi")

#
print(truck == "Ford".lower())


#condicional de desigualdad
print(truck != "audi")# true
print(truck != "ford")# false


#comparaciones numericas
print("comparaciones numericas")
age = 34
print(age == 34) # verdadero True

answer = 17
if answer != 42:
    print("esa no es la respuesta correcta")

# conector menor que <
print("conectores <> <= >=")
age = 19
print(age < 21)#true
print(age <= 21)#true
print(age > 21)#false
print(age >= 21)#false

# multiple conditions
print("multiple conditions")
age_0 = 22
age_1 = 18
print("operacion AND")
print(age_0 >= 21 and age_1 >= 21)# false
print(age_0 >= 21 and age_1 >= 18)# true

print("operacion OR")
print(age_0 >= 21 or age_1 >= 21)# true
print(age_0 >= 23 or age_1 >= 21)# false

# ¿como saber si un elemento esta en una lista?
food = ["chilaquiles", "flautas", "gorditas", "tamales"]
print("\n nopales esta en la lista?")
print("nopales" in food) # false
print("\n gorditas esta en la lista")
print("gorditas" in food) # true

# ¿como saber si un elemento NO esta en una lista?
banned_user = ["andrew", "carolina", "david"]
user = "marie"
print(user not in banned_user)# true

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

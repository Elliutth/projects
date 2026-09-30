#agregar elementos a una lista
motorcycles = ["honda","mortalica","yamaha"]
print(motorcycles) #["honda", "mortalica", "yamaha"]

#metodo apend
motorcycles.append("kawasaki")
print(motorcycles) #["honda", "mortalica", "yamaha", "kawasaki"]

"""
el metodo append ayuda a crear listas
facilmente de manera dinamica
"""
motorcycles_2 = []
print(motorcycles_2)

motorcycle = "ducati"
motorcycles_2.append(motorcycle)
motorcycles_2.append("yamaha")
motorcycles_2.append("suzuki")
print(motorcycles_2)
motorcycle = "charly"
motorcycles_2.append(motorcycle)
print(motorcycles_2)

# el metodo insert nos ayuda a agregar elementos 
# a una lista en un indice especifico
motorcycles_3 = ["honda", "yamaha", "susuki"]
print("\nlista original")
print(motorcycles_3)
motorcycles_3.insert(1,"ducati")
print("lista despues de el metodo insert")
print(motorcycles_3)

## Metodo .pop() Ellimina el ultimo elemento de una lista
# pero nos permite usar el elemento despues de eliminarlo
motorcycles_4 = ["honda", "suzuki", "hd", "mortalica",]
print(motorcycles_4)
deleted_motorcycle = motorcycles_4.pop()
print(f"tu motocicleta borrada es: {deleted_motorcycle}")
print(motorcycles_4)

# Se puede utilizar tambien para eliminar un elemento especifico.
motorcycles_5 = ["honda", "suzuki", "hd", "mortalica",]
print(motorcycles_5)
motorcycles_5.pop(0)
print(motorcycles_5) #lista sin honda
# Metodo .Remove() permite elliminar elementos por su valor.

motorcycles_6 = ["honda", "yamaha", "suzuki", "ducati",]
print(motorcycles_6)
motorcycles_6.remove("yamaha")
print(motorcycles_6)

# Ordenar listas
car = ["bmw", "audi", "toyota", "subaru"]
print(car)
car.sort() #ordenar listas de manera permanente
# argumento opcional de sort(reverse=true)
print(car)
#tarea estudiar el metodo de las listas reverse
#estudiar metodos build-in sorted(), len()
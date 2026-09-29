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
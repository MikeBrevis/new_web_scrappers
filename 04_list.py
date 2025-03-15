#Listas 
#Forma ordenada de agrupar datos

my_list = list()
my_other_list = [20, 50, 48, 52, 69, 70]

print(my_other_list)
print(len(my_other_list))

my_other_list = [20, 1.77, "Mike", "Brevis"]

print(my_other_list[2])
print(my_other_list[3])
print(my_other_list[1])
print(my_other_list[0])
print(my_other_list[2:]) # ['Mike', 'Brevis']  from position two onwards
print(my_other_list[:3]) # [20, 1.77, 'Mike']  from position three backwards

print("Mi nombre es " + my_other_list[2] + " Y mi apellido es " + my_other_list[-1]) # -1 es el ultimo dato de la lista, se considera -2 al penultipo y asi sucesivamente
print("Mido " + str(my_other_list[-3]))


edad, estatura, nombre, apellido = my_other_list
print(nombre + " " + apellido)

my_other_list.append("paila marina") #Inserta un nuevo elemento a la lista
print("Mi plato favorito es " + my_other_list[4])

my_other_list.insert(1, 35) #Inserta un elemento despues de la posicion indicada
print(my_other_list)

my_other_list.remove("Mike") #Elimina un elemento especifico de la lista
print(my_other_list)

print(my_other_list.pop())#Elimina el ultimo elemento del indice por default, ademas se puede eliminar un elemento indicando el indice ej. .pop(2). Puede devolver el valor indicado
print(my_other_list)

my_new_list = [1, 5, 3, 9]

my_new_list.sort() #Ordena de menor a mayor
print(my_other_list)

print(my_new_list)
my_new_list.reverse() #Invierte el orden de las listas
print(my_new_list)











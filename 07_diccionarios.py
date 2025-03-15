#Diccionarios
#Define clave valor en diferentes pares de datos

my_dict = {}

my_other_dict = {
    "Nombre":"Mike", 
    "Apellido":"Brevis", 
    "Edad":35,
    "Lenguaje": {"Phyton", "JS"}  #Contiene un set dentro del diccionario
    }

print(my_other_dict["Apellido"]) #Accede al valor del dato

#Cambiar un elemento
other_name = my_other_dict["Nombre"] = "Juan"
print(my_other_dict["Nombre"])

#Eliminar un elemento
del my_other_dict["Edad"]
print(my_other_dict)

#Buscar un dato 
print("Nombre" in my_other_dict)

#Mas propiedades

""" 
my_other_dict = {
    "key":"value", 
    } 
"""

print(my_other_dict.items()) #Listado con cada uno de los items 
print(my_other_dict.keys()) #Listado con cada una de las llaves
print(my_other_dict.values()) #Listado con cada uno de los valores 

my_new_dict = dict.fromkeys((my_other_dict))#Crea una copia con las llaves del diccionario
print(my_new_dict) 






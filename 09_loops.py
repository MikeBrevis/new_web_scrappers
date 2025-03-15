#Loops

#While: Se repite bajo una condición

my_condition = 0

while my_condition <= 20:
    print(my_condition)
    my_condition += 1
    
    if my_condition == 16:
        print("El numero es 16")
        break                       #Corta el ciclo 

else:
    print("El numero no esta en el rango")

print("Se termina el codigo")

# For: Se ejecuta tantas veces como elementos tenga

my_dict = {
    "Nombre":"Mike", 
    "Apellido":"Brevis", 
    "Edad":35,
    "Lenguaje": {"Phyton", "JS"}  
    }

for element in my_dict:
    print(element)

else:
    print("Finaliza el diccionario")


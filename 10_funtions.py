# Funciones

# Encapsulan una logica en concreto que se puede invocar. Evita el duplicado de codigo

def my_funtion ():
    print("This is a funtion")

my_funtion ()


def sum_values (first_value, second_value):
    print (first_value + second_value)

sum_values (5, 7)


#Funciones con return

#1
def other_values (first, second):
    return first + second

sum_other_values = other_values (10, 5)
print (sum_other_values)

def saludar (nombre):
    return f"Hola, {nombre}!"

#2
mensaje = saludar("Mike")
print(mensaje)

def reprobo (nombre, apellido):
    return f"El alumno {nombre} {apellido} reprobo"

alumno1 = reprobo("alexis", "sanchez")
print (alumno1)

#Funciones con multiples parametros

def print_texts (*texts): #el * permite leer multiples parametros 
    for i in texts:
        print(i.upper())

print_texts("Hola", "que tal", "adios")



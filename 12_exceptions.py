#exceptions

numberOne = 5
numberTwo = 2
numberTwo = "2"

#Try y except son complementarios
try:
    print(numberOne + numberTwo) # error al sumar un numero con un string
    print("No se ha producido un error")

except:
    print("Se ha producido un error")

#Opcional

else:
    print("El codigo continua") # Se ejecuta si el try funciona

finally: # Se ejecuta siempre
    print("La ejecución continua") 

# Captura de la informacion de la excepción

try:
    print(numberOne + numberTwo) # error al sumar un numero con un string
    print("No se ha producido un error")

except ValueError as error:
    print(error)

except Exception as random_error:
    print(random_error)








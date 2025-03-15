#strings

my_string = "mi string"
my_other_string = "mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string) #Se agrega un espacio con " "

 #Formateo de strings

name, surname , age = "mike", "brevis", 35
print("mi nombre es {} {} y mi edad es {}" .format(name, surname, age)) #opcion con .format
print("mi nombre es %s %s y mi edad es %d" %(name, surname, age)) #opcion con %
print("mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) #Practica no recomendada ya que es poco segura
print(f"mi nombre es {name} {surname} y mi edad es {age}") #f formatea e infiere el valor de las variables

#Desenpaquetado de caracteres
lenguage = "python"
a, b, c, d, e, f = lenguage

print(a)
print(f)

#Metodos y funciones // averiguar las mas importantes
print(lenguage.capitalize()) #Primera letra en mayuscula
print(lenguage.count("t")) #Cuenta caracteres especificos
print(lenguage.isnumeric()) #Indica si es un numero
print(lenguage.upper()) #Transforma todo a mayusculas








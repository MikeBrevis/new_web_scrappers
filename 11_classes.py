# Classes // repasar

#Crea objetos concretos que heredan caracteristicas y comportamientos.

class person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"
    
    def walk (self):                                # Define una funcion con una clase
        print(f"{self.full_name} esta caminando")

my_person = person("mike", "brevis")
print(my_person.full_name)
my_person.walk()






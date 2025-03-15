#Lista de elementos que no se pueden modificar, a diferencia de las listas

my_tuple = (30, 1.77, "brais", "moure", "brais") #Al declararse en () es una tupla
print(my_tuple)
print(type(my_tuple))

print(my_tuple.count("brais"))
print(my_tuple.index("brais"))

#No se puede cambiar los valores de la tupla asignando una nueva variable al contador indicado.
""" my_tuple[1] = 1.80
print(my_tuple) """



# variables
my_string_variable = "hello world"
print(my_string_variable)

my_int_variable = 10
print(my_int_variable)

my_float_variable = 10.5
print(my_float_variable)

my_bool_variable = True
print(my_bool_variable)

#variables concatenation in print
print(my_string_variable, my_int_variable, my_float_variable, my_bool_variable) 
print(type(my_string_variable), type(my_int_variable), type(my_float_variable), type(my_bool_variable))

#sistem funtions
print(len(my_string_variable))
print("This is the value of the variable `my_string_variable`:", (len(my_string_variable)))

#its possible to print more than one variable on the same line, but in not a good practice
name, surname = "John", "Doe"
print(name, surname)

#inputs
name = input("What is your name? ")
print("Hello", name)

# ID variables // The ID is relative to value os the variable

k = 10
print(id(k))

a = 10
print(id(a))



#Variables

my_string_variable = "My variable String"
print(my_string_variable)

my_init_variable = 5
print(my_init_variable)

my_in_to_variable = str(my_init_variable)
print(my_in_to_variable)
print(type(my_in_to_variable))

my_bool_varial = False
print(my_bool_varial) 
#concatenación de variables en un print
print(my_string_variable , my_in_to_variable , my_bool_varial)
print("Este es el valor de:", my_bool_varial)

#Algunas funciones del sistema
print(len(my_string_variable))

#Variable en una sola linea !Cuidado con abusar de esta sintaxis
name, surname,alias,edad = "Jhon" , "davila" , "nito", 28
print("Me llamo ",name , surname, ", mi alias es" , alias , "y mi edad es", edad)
#inputs
firs_name = input('cual es u nombre? ')
age= input('cual es ttu edad? ')

print(firs_name)
print(age)
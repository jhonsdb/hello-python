### SETS ###

"""
Un set es una estructura no ordenada
Características
No tienen índices.
No permiten duplicados.
Muy útiles para operaciones matemáticas.
Permiten agregar y eliminar elementos.
"""

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))#Inicialmente es un Dicionario

my_other_set = {"Jhon","Davila",28}
print(type(my_other_set))

print(len(my_other_set)) #3

#print(my_other_set[0]) #error en lista si es posibble en este caso no es posible
my_other_set.add("nito")
print(my_other_set)#Un set no es una estrucutra ordenada

print("nito" in my_other_set)
print("niti" in my_other_set)

my_other_set.remove("nito")
print(my_other_set)

my_other_set.clear()#elimina el conttenido pero mantenemos el set
print(my_other_set)


del my_other_set #elimina la variable
#print(my_other_set)#NameError: name 'my_other_set' is not defined

my_set = {"Jhon","Davila",28}
my_list = list(my_set)
print(my_list[0])

my_other_set = {"Kotlin","JS","Python"}

my_new_set = my_set.union(my_other_set)# para unir dos set
print(my_new_set)
print(my_new_set.union({"C#", "Vue"}))

print(my_new_set.difference(my_set))
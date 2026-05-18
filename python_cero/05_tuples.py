###TUPLAS
# Características
"""
No se pueden cambiar después de crearse.
Permiten duplicados.
Más rápidas que las listas.
Se usan para datos constantes
"""
# 
# ###
#conjunto de valores 


my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35,1.77,"jhon","davila","jhon","davila")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("jhon"))#cuenta y me devuelve la plabra de elemetos que tengo dentro de la tupla
print(my_tuple.index("davila"))#me dice enn que indice sse encuntra la plabra "davila" en este caso 
#en el caso de haber dos iguales devuelve el primero que encuntra

#my_tuple[1] = 1.80 #la lista en el indice 1 se cambiaria pero al ser tupla no me permite cambiarlo por lo que sale es un Error

my_sum_tupla = my_tuple + my_other_tuple
print(my_sum_tupla) 
print(my_sum_tupla[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "caridad"
my_tuple.insert(1,"Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion
del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined
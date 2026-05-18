### Dictionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Jhon", "Apellido":"Davila", "Edad":28, 1:"Python"}


my_dict = {
    "Nombre":"Jhon", 
    "Apellido":"Davila", 
    "Edad":28, 
    "Lenguajes":{"Python", "Swift", "Kotlin"},
    1:1.65
    }

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))


print(my_dict["Nombre"]) 
my_dict["Nombre"] = 'Stiven'
print(my_dict)

print(my_dict[1])

my_dict["Calle"] = "gta" #ASI AÑADIMO UN NNUEVO CAMPO AL DICCIONARIO
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Nombre" in my_dict)
print("Stive" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())


my_new_dic = my_other_dict.fromkeys(("Nombre", 1 , "Piso"))
print(my_new_dic)


my_new_dic = dict.fromkeys(my_dict)
print(my_new_dic)
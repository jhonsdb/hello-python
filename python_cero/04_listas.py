#LISTAS/LISTS#\

my_list = list()
my_other_list = []




my_list = [35,24,62,52,30,30,17]

print(my_list)
print(len(my_list))

my_other_list  = [35,1.77, "jhon",'davila']

print(type(my_other_list))
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
#print(my_other_list[4]) IndexError
#print(my_other_list[-4]) IndexError

age,height,name,surname = my_other_list
print(name)

my_other_list.append("caridad")
my_other_list.insert(1,"azul")
my_other_list.remove("azul")
print(my_other_list)


print(my_list)
my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)


my_list = "hola python"
print(my_list)
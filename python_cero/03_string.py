### Strings ###
my_string = 'mi srting'
my_other_string = "mi otro srting"

print(len(my_string))
print(len(my_other_string))

print(my_string + "  " + my_other_string)

my_new_line_srting = "Este es un nuevo \ncon slyto de linea"
print(my_new_line_srting)

myt_tab_string = "\tEstet es un string con tabulacion"
print(myt_tab_string)

my_scape_string = "\\t Eset es un strting \\n escapado"
print(my_scape_string)

#formateo
name , surname, age = "jhon" , "davila" , 28 

print("mi nombre es {} {} y mi edad esd {}".format(name,surname,age))
print("mi nombre es %s %s y mi edad esd %d" %(name,surname,age))
print(f"mi nombre es {name} {surname} y mi edad esd {age}")


#DESEMPQUETADO DE CARACTERES
language = "python"
a, b ,c,d,e,f= language
print(a)
print(b)

#diviison
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

#REVERSE
reverse_language = language[::-1]
print(reverse_language)

#FUNCIONES

print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.startswith("py"))

print(language.upper().isupper())
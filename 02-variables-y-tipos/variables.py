<<<<<<< Updated upstream
"""
una variables en un contenedor de informacion
que dentro guarda un dato, se puede crear
muchas variables y que cada una tenga un dato distinto
"""

texto = "Master"

print(texto)

print("-----------------------------------------")

#concatenacion
nombre = "Luis"
apellido = "Capello"
apellido2 = "Estrada"

print(nombre + " "  + apellido + " " + apellido2)
print(f"{nombre} {apellido} {apellido2}")
print("hola me llamo {} {} {}".format(nombre,apellido,apellido2))

def print_alpha_nums( abc_list, num_list):
    for char in abc_list:
        for num in num_list:
            print(char, num)
    return
=======
"""
una variables en un contenedor de informacion
que dentro guarda un dato, se puede crear
muchas variables y que cada una tenga un dato distinto
"""

texto = "Master"

print(texto)

print("-----------------------------------------")

#concatenacion
nombre = "Luis"
apellido = "Capello"
apellido2 = "Estrada"

print(nombre + " "  + apellido + " " + apellido2)
print(f"{nombre} {apellido} {apellido2}")
print("hola me llamo {} {} {}".format(nombre,apellido,apellido2))

def print_alpha_nums( abc_list, num_list):
    for char in abc_list:
        for num in num_list:
            print(char, num)
    return
>>>>>>> Stashed changes
print_alpha_nums(['a','b','c'],[1,2,3])
NOMBRE = "Juan"
APELLIDO = "Perez"
edad = "30"

# Concatenación de cadenas con el operador "+"
primerosDatosPersonales = "Mi nombre es: " + NOMBRE + "\nMi apellido es: " + APELLIDO + "\nMi edad es: " + edad
print(primerosDatosPersonales)

# Concatenación de cadenas con el operador "%"
segundosDatosPersonales = "Mi nombre es: %s \nMi apellido es: %s \nMi edad es: %s" % (NOMBRE, APELLIDO, edad)
print(segundosDatosPersonales)

# Concatenación de cadenas con el método "format()"
tercerosDatosPersonales = "Mi nombre es: {} \nMi apellido es: {} \nMi edad es: {}".format(NOMBRE, APELLIDO, edad)
print(tercerosDatosPersonales)
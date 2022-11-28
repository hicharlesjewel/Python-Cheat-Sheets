# Python-Cheat-Sheets

Hojas de trucos para aprender Python.

## Comentarios

```python
# Comentarios en linea con usando un "#" hashtag.
'''Comentarios multilíneas
con triples "'" comillas simples
al inicio y final del comentario.'''
```

## Imprimir

```python
# Imprimir en la consola
print("Hola mundo!")
```

## Salto de línea

```python
# Salto de línea
print("Hola \n mundo!")
```

## Tipo de datos

### Números

```python
# Números enteros
3
# Números de punto flotante
3.14
# Números complejos
3 + 4j
```

### Cadenas

```python
# Cadenas de caracteres con comillas dobles
"Esto es una cadena de caracteres."
# Cadenas de caracteres con comillas simples
'Esto es una cadena de caracteres.'
# Cadenas de caracteres con tres comillas dobles
"""Esto es una cadena de caracteres."""
# Cadenas de caracteres con tres comillas simples
'''Esto es una cadena de caracteres.'''
```

### Listas

```python
# Listas
[1, 2, 3]
# Listas con diferentes tipos de datos
[1, "dos", 3.14]
```

### Tuplas

```python
# Tuplas
(1, 2, 3)
# Tuplas con diferentes tipos de datos
(1, "dos", 3.14)
```

### Diccionarios

```python
# Diccionarios
{"uno": 1, "dos": 2, "tres": 3}
# Diccionarios con diferentes tipos de datos
{"uno": 1, "dos": "dos", "tres": 3.14}
```

### Conjuntos

```python
# Conjuntos
{1, 2, 3}
# Conjuntos con diferentes tipos de datos
{1, "dos", 3.14}
```

### Booleanos

```python
# Booleanos
True
False
```

### Nulos

```python
# Nulos
None
```

## Variables

```python
# Variables en Python son dinámicas, no se necesita declarar el tipo de variable.

# Asignación de variables
x = 1
y = 2
z = 3

# Asignación múltiple
x, y, z = 1, 2, 3

# Asignación múltiple con el mismo valor
x = y = z = 1

# Asignación de variables con valores de diferentes tipos
x, y, z = 1, 2.0, "3"

# Asignación de variables con valores de diferentes tipos
x = 1
y = 2.0
z = "3"
```

## Constantes

```python
# Constantes en Python son variables que no cambian su valor.

# Por convención, se escriben en mayúsculas.

PI = 3.14159
GRAVEDAD = 9.8
```

## Concatenación

### Números

```python
# Concatenación de números con el operador "+"
x = 1
y = 2
z = x + y
print(z) # 3

# Concatenación de números con el operador "%"
x = 1
y = 2
z = "%s + %s = %s" % (x, y, x + y)
print(z) # 1 + 2 = 3

# Concatenación de números con el método "format()"
x = 1
y = 2
z = "{} + {} = {}".format(x, y, x + y)
print(z) # 1 + 2 = 3
```

### Cadenas

```python
# Concatenación de cadenas con el operador "+"
NOMBRE = "Juan"
APELLIDO = "Perez"
edad = "30"
datosPersonales = "Mi nombre es: " + NOMBRE + " Mi apellido es: " + APELLIDO + " Mi edad es: " + edad
print(datosPersonales) # Mi nombre es: Juan Mi apellido es: Perez Mi edad es: 30

# Concatenación de cadenas con el operador "%"
NOMBRE = "Juan"
APELLIDO = "Perez"
edad = 30
datosPersonales = "Mi nombre es: %s Mi apellido es: %s Mi edad es: %s" % (NOMBRE, APELLIDO, edad)
print(datosPersonales) # Mi nombre es: Juan Mi apellido es: Perez Mi edad es: 30

# Concatenación de cadenas con el método "format()"
NOMBRE = "Juan"
APELLIDO = "Perez"
edad = 30
datosPersonales = "Mi nombre es: {} Mi apellido es: {} Mi edad es: {}".format(NOMBRE, APELLIDO, edad)
print(datosPersonales) # Mi nombre es: Juan Mi apellido es: Perez Mi edad es: 30
```

### Listas

```python
# Concatenación de listas con el operador "+"
x = [1, 2, 3]
y = [4, 5, 6]
z = x + y
print(z) # [1, 2, 3, 4, 5, 6]

# Concatenación de listas con el operador "*"
x = [1, 2, 3]
y = x * 3
print(y) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### Tuplas

```python
# Concatenación de tuplas con el operador "+"
x = (1, 2, 3)
y = (4, 5, 6)
z = x + y
print(z) # (1, 2, 3, 4, 5, 6)

# Concatenación de tuplas con el operador "*"
x = (1, 2, 3)
y = x * 3
print(y) # (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

### Diccionarios

```python
# Concatenación de diccionarios con el operador "+"
x = {"uno": 1, "dos": 2, "tres": 3}
y = {"cuatro": 4, "cinco": 5, "seis": 6}
z = x + y
print(z) # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# Concatenación de diccionarios con el operador "*"
x = {"uno": 1, "dos": 2, "tres": 3}
y = x * 3
print(y) # TypeError: unsupported operand type(s) for *: 'dict' and 'int'
```

### Conjuntos

```python
# Concatenación de conjuntos con el operador "+"
x = {1, 2, 3}
y = {4, 5, 6}
z = x + y
print(z) # TypeError: unsupported operand type(s) for +: 'set' and 'set'

# Concatenación de conjuntos con el operador "*"
x = {1, 2, 3}
y = x * 3
print(y) # TypeError: unsupported operand type(s) for *: 'set' and 'int'
```

### Booleanos

```python
# Concatenación de booleanos con el operador "+"
x = True
y = False
z = x + y
print(z) # TypeError: unsupported operand type(s) for +: 'bool' and 'bool'

# Concatenación de booleanos con el operador "*"
x = True
y = False
z = x * 3
print(z) # TypeError: unsupported operand type(s) for *: 'bool' and 'int'
```

### Nulos

```python
# Concatenación de nulos con el operador "+"
x = None
y = None
z = x + y
print(z) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

# Concatenación de nulos con el operador "*"
x = None
y = None
z = x * 3
print(z) # TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
```

### Diferentes tipos de datos

````python
# Concatenación de diferentes tipos de datos con el operador "+"
x = 1
y = 2.0
z = "3"
w = x + y + z
print(w) # TypeError: unsupported operand type(s) for +: 'float' and 'str'

# Concatenación de diferentes tipos de datos con el operador "%"
x = 1
y = 2.0
z = "3"



## Operadores

### Operadores aritméticos

```python
# Suma
3 + 2
# Resta
3 - 2
# Multiplicación
3 * 2
# División
3 / 2
# División entera
3 // 2
# Módulo
3 % 2
# Exponente
3 ** 2
````

### Operadores de asignación

```python
# Asignación
x = 3
# Asignación de suma
x += 3
# Asignación de resta
x -= 3
# Asignación de multiplicación
x *= 3
# Asignación de división
x /= 3
# Asignación de división entera
x //= 3
# Asignación de módulo
x %= 3
# Asignación de exponente
x **= 3
```

### Operadores de comparación

```python
# Igual
3 == 2
# No igual
3 != 2
# Mayor que
3 > 2
# Menor que
3 < 2
# Mayor o igual que
3 <= 2
# Menor o igual que
3 >= 2
```

### Operadores lógicos

```python
# AND
True and False
# OR
True or False
# NOT
not True
```

### Operadores de identidad

```python
# IS
3 is 2
# IS NOT
3 is not 2
```

### Operadores de membresía

```python
# IN
3 in [1, 2, 3]
# NOT IN
3 not in [1, 2, 3]
```

## Funciones

### Funciones integradas

```python
# Imprimir
print("Hola mundo")
# Longitud
len("Hola mundo")
# Tipo de dato
type("Hola mundo")
# Conversión a entero
int("3")
# Conversión a flotante
float("3.14")
# Conversión a cadena
str(3)
# Conversión a lista
list((1, 2, 3))
# Conversión a tupla
tuple([1, 2, 3])
# Conversión a diccionario
dict([("uno", 1), ("dos", 2), ("tres", 3)])
# Conversión a conjunto
set([1, 2, 3])
```

### Funciones definidas por el usuario

```python
# Definición de función
def funcion():
    print("Hola mundo")
# Llamada a función
funcion()
```

## Estructuras de control

### Condicional if

```python
# Condicional if
if 3 > 2:
    print("3 es mayor que 2")
```

### Condicional if-else

```python
# Condicional if-else
if 3 > 2:
    print("3 es mayor que 2")
else:
    print("3 no es mayor que 2")
```

### Condicional if-elif-else

```python
# Condicional if-elif-else
if 3 > 2:
    print("3 es mayor que 2")
elif 3 < 2:
    print("3 es menor que 2")
else:
    print("3 es igual a 2")
```

### Bucle for

```python
# Bucle for
for i in [1, 2, 3]:
    print(i)
```

### Bucle while

```python
# Bucle while
i = 1
while i <= 3:
    print(i)
    i += 1
```

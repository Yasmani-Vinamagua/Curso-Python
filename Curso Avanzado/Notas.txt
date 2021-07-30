modulo -> Es cualquier archivo de Python. Generalmente, contiene código que puedes reutilizar
paquete -> Es una carpeta que contiene módulos. Siempre posee el archivo _init_.Python

¿Qué son los tipados?
Es una clasificación de los lenguajes de programación. Existen 4 tipos:
 - Estático
 - Dinámico
 - Débil
 - Fuerte

Para declarar variables desde python 3.6:
 - a: int = 5
 - b: str = "hola"
 - c: bool = True

Para trabajar con tipos con estructura de datos de manera estandar es importar las clases Dict y List
 - from typing import Dict, List

Para trabajar con tuplas
 - from typing import Tuple

mypy -> módulo que permite trabajar con tipos en paython y muestra los errores en consola. Se complementa con el módulo typing

*Pasos para crear nuevo proyecto*
 1 Crear la carpeta donde se va a trabajar
 2 Ejecutar -> git init en la carpeta 
 3 Ejecutar -> py -m venv venv
 4 Crear archivo -> .gitignore
 5 Dentro de .gitignore colocar -> venv/
 6 Entrar al entorno virtual -> .\venv\Scripts\activate
 7 Instalar el módulo de error -> pip install mypy
 8 Crear el archivo .py y comenzar a trabajar
 9 Ejecutamos el código creado -> py nombre_archivo.py
 10 Para que se nos muestre de mejor forma los errores ejecutamos -> mypy nombre_archivo.py --check-untyped-defs
 
Scope -> Es el alcance de las variables - Se pueden crear variables local y global con el mismo nombre pero con diferentes valores
 - Local Scope -> Alcance de las variables dentro de nuestro bloque
 - Global Scope -> Las variables estan disponibles en todas las funciones

Closueres
Nested functions -> Son funciones dentro de otras funciones.
Clousures -> Se da cuando una variable que está en un scope superior es recordada por una función que está en un scope inferior, aunque el scope superior sea eliminado.
Reglas para encontrar un clousure:
 - Debemos tener una nested function
 - La nested function debe referenciar un valor de un scope superior 
 - La función que envuelve a la nested function debe retornarla también.
¿Dónde aparecen? -> En clases cortas y cuando trabajamos con decoradores.

Decoradores -> Es una función que recibe como parámetro otra función, le añade cosas y retorna una función diferente.

Iterables -> Todos los objetos que podemos recorrer en un ciclo, ejem: una lista, un string
Iteradores -> Ahorra recursos, puedo almacenar secuencias y progreciones matematicas, ocupa poca memoria.

Generadores -> Son funciones que guardan un estado. Sugar syntax de los iteradores. Tiene las ventajas de un iterador pero mas facil

List comprehension -> Almacena todos los elementos en memoria 

Generator expresion -> Saca uno por uno los elementos

sets -> son una colección desordenada de elementos únicos e inmutables

Añadir elementos en un set -> .add - .update

Remover o quitar elementos de un set -> .remove - .discard - .pop - .clear

Operaciones con sets 
 - Union -> |
 - Intersección -> &
 - Diferencia -> -
 - Diferencia Simetrica -> ^

Manejo de fechas
 - import datetime
 - my_time = datetime.datetime.now()
 - my_time = datetime.date.today()
 - my_day.year - my_day.month - my_day.day

Times zones
 1 pip install pytz -> en consola
 2 from datetime import datetime
 3 import pytz
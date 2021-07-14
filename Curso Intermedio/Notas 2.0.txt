- El zen de Python
    import this = Se coloca el comando en la consola y nos muestra el zen de Python

- Documentacion de python 
    https://docs.python.org/3/
    Los PEP Index nos dicen como funciona el lenguaje y como deberiamos escribirlos de forma correcta

- Un modulo es un codigo escrito por otra persona que nos ahorra tiempo y se lo puede implementar

- Crear un ambiente virtial VENV
    1.- py -m venv nombre_virtual #Usualemente el nombre virtaul es "venv"
    2.- .\venv\Scripts\activate #Activa el ambiente virtual 
    3.- deactivate #Salir del ambiente virtual
    4.- alias avenv=.\venv\Scripts\activate #Crear alias para la accion de activar ambiente virtual

- Instalación de dependencias con PIP
    1.- Activamos el ambiente virtual con el comando "avenv"
    2.- pip freeze #Muetsra los modulos instalados 
    3.- pip install pandas #Instala el modulo pandas
    4.- pip freeze > requirements.txt #Guardar las dependecias con sus versiones para poder compartirlas en GitHub
    5.- cat requirements.txt #Ver el contenido del archivo 
    6.- pip install -r requirements.txr #Instalar las dependencias que se guardaron en el archivo (para la persona a la que se le comparte el proyecto)

- Anaconda
    Especial para ciencia de datos, no recomendado para otro campo.
    1.- Instalamos Anaconda
    2.- Ejecutamos anaconda.navigator
    3.- Enviroments > Create > Asignamos nombre y esocogemos el lenguaje > Create
    4.- Install > All > Update Index
    5.- Search > Escribe "pandas" > Selecionamos "pandas" > Apply > Apply

code . #Inicializar Studio code

- List comprehensions
    Estructura: [element for element in interable if condition]
    
- Dictionary comprehensions
    Estructura: {key:value for value in interable if condition}

- Funciones anónimas: lambda
    Estructura: lambda argumentos: expresión

- | Este simbolo une un diccionario con otro nuevo

- Errores
    . SyntaxError
    . Exception {KryboardInterrupt, KayError, IndexError, FileNotFoundError, ZeroDivisionError, ImportError}

- Debugging
    1.- Ejecución y depuración
    2.- Python file
    3.- Con boton de pausa detenemos el programa donde queremos
    4.- Con voton depurar paso a paso vemos como avanza el codigo linea por linea
    5.- Con voton depurar paso a paso por instrucciones vamos al origen del codigo para revisarlo
    6.- Colocando circulo rojo al ejecutar se detenine el programa en esa linea

- Manejo de excepciones
    TRY: En el try se coloca código que esperamos que pueda lanzar algún error.
    EXCEPT: En el except se maneja el error, es decir, si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.
    ELSE: El else se ejecuta sólo si no hubo ninguna excepción lanzada desde el try
    FINALLY: Se ejecuta SIEMPRE, haya sido lanzada la excepción o no haya sido lanzada.

- Assert statements
    Estructura: assert condición, mensaje de error
    .isnumeric() = devuelve falso si no se ingresa un número y verdadero si se lo hace

- Modos de Apertura
    r -> Solo lectura
    r+ -> Lectura y escritura
    w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
    w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
    a -> Añadido (agregar contenido). Crea el archivo si éste no existe
    a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

- Cómo trabajr con archivos
    with open("./ruta/del/archivo.txt, "r") as f:
    encoding="utf-8" Sirve para que Python pueda soportar caracteres del idioma español, como la “ñ” y letras con tilde.
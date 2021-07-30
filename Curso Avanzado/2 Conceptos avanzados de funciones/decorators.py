from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs): #No importa la cantiodad de argumentos, la funcion va a funcionar con args
        initial_time = datetime.now() #now devuelve la fecha y hora exacta en la que se ejecuta esta linea
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron "+ str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 10000000): # se coloca _ xq no nos interesa la variable de cada vuelta
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre="cesar"):
    print("hola "+ nombre)

suma(5,5)
random_func()
saludo("facundo")
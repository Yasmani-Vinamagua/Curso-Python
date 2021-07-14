# 1.- Ejecución y depuración
# 2.- Python file
# 3.- Con boton de pausa detenemos el programa donde queremos
# 4.- Con voton depurar paso a paso vemos como avanza el codigo linea por linea
# 5.- Con voton depurar paso a paso por instrucciones vamos al origen del codigo para revisarlo
# 6.- Colocando circulo rojo al ejecutar se detenine el programa en esa linea


def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try: 
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError: #Excepción
        print("Debes ingresar un número")

if __name__ == "__main__":
    run()
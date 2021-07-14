def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
        num = input("Ingresa un número: ")
        assert num.isnumeric(), "Debes ingresar un número" #isnumeric devuelve falso si no se ingresa un número y verdadero si se lo hace
        print(divisors(int(num)))
        print("Terminó mi programa")

if __name__ == "__main__":
    run()
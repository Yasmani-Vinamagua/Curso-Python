def read():
    numbers=[]
    with open("C:/Users/YASMANI/Desktop/curso python/Curso Intermedio/Manejo de archivos/archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f: #leer cada linea del archivo
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Facundo", "Miguel", "Pepe", "Cristian", "Rocío"]
    with open("C:/Users/YASMANI/Desktop/curso python/Curso Intermedio/Manejo de archivos/archivos/names.txt", "w", encoding="utf-8") as f: #Crear un arcivo con los datos de names. Se coloca "a" en lugar de "w" para no sobreescribir el txt
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    write()

if __name__ == "__main__":
    run()
import random
import os
from unicodedata import normalize

def clear ():
    os.system("clear")

def read():
    palabras=[]
    with open("C:/Users/YASMANI/Desktop/curso python/Curso Intermedio/Manejo de archivos/archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f: #leer cada linea del archivo
            palabras_normalizadas = line.strip().upper()#quitar espacios y poner en mayuscula
            palabras.append(palabras_normalizadas)
    return palabras

def palabra_escogida():
    palabras=read()
    numero_aleatorio = random.randint(1, 171)
    palabra_elegida=palabras[numero_aleatorio]
    #Quitar las tildes de la palabra
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    palabra_elegida = normalize('NFKC', normalize('NFKD', palabra_elegida).translate(trans_tab))
    return palabra_elegida

def llenar_espacios():
    espacios=[]
    letra_ingresada=[]
    palabra_elegida=list(palabra_escogida())
    numero_letras=len(palabra_elegida)
    #contar los espacios de la palabra
    for i in range(0,numero_letras):
        espacios.append("__")

    #logica del juego
    while espacios != palabra_elegida:
        print("===============================Juego del Ahorcado===============================")
        print("\n")
        print(espacios)
        print("\n")
        print("Numero de letras de la palabra: "+str(numero_letras))
        print("\n")
        letra_ingresada=input(str("Ingresa una letra: "))
        letra_ingresada=letra_ingresada.upper()
        print("Letra ingresada:"+letra_ingresada)
        for j in range(0,numero_letras):
            if letra_ingresada == palabra_elegida[j]:
                espacios[j] = letra_ingresada    
        print(espacios)
        clear()
    print("Felicidades Ganaste")
    print("La Palabra es: "+ str(palabra_elegida))


def run():
    llenar_espacios()
    

if __name__ == "__main__":
     run()
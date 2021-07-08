def run():
    #imprimir solo números pares
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue #no imprimas si se cumple esta condicion
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break #stop cuando se cumpla la condicion

    texto = input("Escribe un texto: ")
    for letra in texto:
        if letra == "o":
            break
        print(letra)
if __name__ == "__main__":
    run()
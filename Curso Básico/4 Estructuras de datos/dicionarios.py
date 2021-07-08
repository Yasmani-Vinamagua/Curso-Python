def run():
    mi_diccionario = {
        "llave1":1,
        "llave2":2,
        "llave3":3,
    }
    # print(mi_diccionario)
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])

    poblacion_paises ={
        "Argentina": 44938712,
        "Brasil": 210147,
        "Colombia": 50372424
    }

    # print(poblacion_paises["Argentina"])

    # for pais in poblacion_paises.keys(): #devuelve el nombre de las llaves
    #     print(pais)

    # for pais in poblacion_paises.values(): #devuelve el comtemido de las llaves
    #     print(pais)

    for pais, poblacion in poblacion_paises.items(): #devuelve llaves y valores
        print(pais+" tiene "+str(poblacion)+" habitantes")
    
    
if __name__ == "__main__":
    run()
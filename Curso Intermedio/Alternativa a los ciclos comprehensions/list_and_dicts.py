def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "facundo", "lastname":"Garcia"}

    #Lista de diccionarios
    super_list = [
        {"firstname": "facundo", "lastname":"Garcia"},
        {"firstname": "fernando", "lastname":"Ocha"},
        {"firstname": "fiorela", "lastname":"Martinex"},
        {"firstname": "fiona", "lastname":"Sherk"},
        {"firstname": "francisco", "lastname":"Lara"}
    ]

    #Discionario de listas
    super_dict = {
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floatinf_nums":[1.1, 4.5, 6.45]
    }

    for item in super_list:
        print(item["firstname"] , "-" , item["lastname"])


    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == "__main__":
    run()
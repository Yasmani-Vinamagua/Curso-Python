def run():
    # my_dict ={}

    # for i in range (1,101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3
    # print (my_dict)

    # Estructura de Dictionary comprehensions {key:value for value in interable if condition}
    # my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0}
    # print (my_dict)

    my_dict = {i:round(i**0.5, 2) for i in range(1,1001) }
    print (my_dict)

if __name__ == "__main__":
    run() 
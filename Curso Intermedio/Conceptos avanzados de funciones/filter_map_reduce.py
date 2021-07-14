def run():

    #Ejemplo de filter
    my_list1 = [1,2,4,5,6,9,13,19,21]
    odd = list(filter(lambda x: x %2 !=0, my_list1))
    print(odd)

    #Ejemplo de map
    my_list2 = [1,2,3,4,5,6]
    squares = list(map(lambda x: x**2, my_list2))
    print(squares)

    #Ejemplo de reduce

    from functools import reduce

    my_list3 = [2,2,2,2,2]
    all_multiplied = reduce(lambda a, b: a*b, my_list3)
    print(all_multiplied)

if __name__ == "__main__":
    run()
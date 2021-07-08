def conversor(tipo_pesos, valor_dolar):
    pesos = input("cuantos pesos "+ tipo_pesos +" tienes?:")
    pesos = float(pesos) #transformar a número con decimales
    dolares=pesos/valor_dolar
    dolares = round(dolares, 2) #número de decimales
    dolares = str(dolares)
    print("Tienes un total de $"+dolares+" dólares")
menu ="""
Bienvenido al conversor de monedas 😂

1 - Pesos colombianos
2 - Pesos argentinso
3 - Pesos mexicanos

Elige una opcion: """

opcion =int(input(menu))
if opcion == 1:
    conversor("colombianos", 3875)
elif opcion ==2:
    conversor("argentinos", 65)
elif opcion ==3:
    conversor("mexicanos", 24)
else:
    print("Ingresa una opción por favor")


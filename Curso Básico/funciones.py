# def imprimir_mensaje(): #asi se define una funcion
#     print("mensaje especial: ")
#     print("estoy aprendiendo a usar funciones")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()
#---------------------------------------------------------------
# def conversacion(mensaje):
#     print ("Hola")
#     print ("Cómo estás")
#     print (mensaje)
#     print ("Adios")

# opcion= int(input("elige una opcion (1, 2, 3):"))
# if opcion == 1:
#     conversacion("elegiste la opcion 1")
# elif opcion ==2:
#     conversacion("elegiste la opcion 2")
# elif opcion == 3:
#     conversacion("elegiste la opcion 3")
# else:
#     print ("Elige la opción correcta")
#-----------------------------------------------------------------
def suma (a, b):
    print("Se suman dos números")
    resultado =a+b
    return resultado #devuelve la variable resultado
sumatoria = suma(1, 4)
print (sumatoria)
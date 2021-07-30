# Ejemplo inicial
#import time 

# def fibo_gen():
#     n1 = 0
#     n2 = 1
#     counter = 0
#     while True:
#         if counter == 0:
#             counter +=1
#             yield n1 
#         elif counter == 1:
#             counter += 1
#             yield n2
#         else: 
#             aux = n1 + n2
#             n1, n2 = n2, aux
#             counter += 1
#             yield aux

# if __name__ == "__main__":
#     fibonacci = fibo_gen()
#     for element in fibonacci:
#         print(element)
#         time.sleep(1)

#Simplificado y con número máximo
from time import sleep

def fibonacci_gen(max_counter:int):
    a, b = 0, 1
    while a <= max_counter:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    for element in fibonacci_gen(39):
        print(element)
        sleep(0.3)
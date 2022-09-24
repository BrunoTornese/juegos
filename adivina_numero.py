import random


def adivina_el_numero(x):
    print('---------------------------------------------')
    print('Hola! estas en el juego de adivinar el numero')
    print('---------------------------------------------')
    print('Intenta adivinar el numero que estoy pensando')
    numero_secreto= random.randint(1,x)#genera un numero aleatorio entre 1 y x
    prediccion= 0#numero que se ingresa por el usuario
    while prediccion != numero_secreto:#mientras que el numero no sea el correcto
        prediccion= int(input(f'El numero se encuentra entre 1 y {x}: '))#pide un numero al usuario entre el 1 y el valor de x
        if prediccion > numero_secreto:#si el numero es mayor al numero secreto
            print('El numero es menor')#imprime que el numero es menor
        elif prediccion < numero_secreto:#si el numero es menor al numero secreto
            print('El numero es mayor')#imprime que el numero es mayor
        else:#si el numero es igual al numero secreto
            print(f'Felicidades! adivinaste el numero secreto!! este era: {numero_secreto}')#imprime felicidades
            break#sale del ciclo
    


adivina_el_numero(1000)#llama a la funcion adivina_el_numero con el valor de x=10

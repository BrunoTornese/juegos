import random

def jugar():
    usuario=input("Elige piedra, papel o tijera: ").lower()#El usuario elige piedra, papel o tijera
    computadora=random.choice(["piedra","papel","tijera"])#La computadora elige piedra, papel o tijera
    if usuario==computadora:#Si el usuario y la computadora son iguales
        return "Empate!!!"

    if gano_el_jugaror(usuario,computadora):#Si gana el jugador
        return "Ganaste!!!"
    else:#Si pierde el jugador
        return "Perdiste!!!"
   

def gano_el_jugaror(usuario,computadora):
    if usuario=="piedra" and computadora=="tijera":#Si el usuario elige piedra y la computadora elige tijera
        return True#Gana el jugador
    elif usuario=="papel" and computadora=="piedra":#Si el usuario elige papel y la computadora elige piedra
        return True#Gana el jugador
    elif usuario=="tijera" and computadora=="papel":#Si el usuario elige tijera y la computadora elige papel
        return True#Gana el jugador
    else:#Si no gana el jugador
        return False#Pierde el jugador


print(jugar())#Imprime el resultado de la partida
import random
import time
from os import system


def cabecera():
    system("cls")
    print("-------------------------------")
    print("|    ADIVINA EL NUMERO        |")
    print("-------------------------------")
    print("\n")

def barra():
    cabecera()
    print("Voy a pensar un número del 1 al 10... a ver si lo adivinas.")
    print("Puedes seguir jugando hasta agotar tu crédito,")
    print("¡SUERTE!")
    car = "📗"
    distancia = 10
    for position in range(distancia):
        print("📗" * position, end="")
        print(car, end="\r")
        time.sleep(0.5)
    print("📗" * distancia, "   YA, adelante")
    time.sleep(1.5)

def inicializar_creditos():
    cabecera()
    creditos = 0
    while creditos == 0:
        monedas = float(input("Introduce monedas\n1- 50 cts para 1 crédito.\n2- 1 € para 3 créditos\n0- Apagar Sistema\n"))
        match monedas:
            case 1:
                creditos = creditos + 1
            case 2:
                creditos = creditos + 3
            case 0:
                print("Apagando sistema...")
                exit()
    return creditos

def jugar(creditos, usuario):
    marcador = 0
    repetir = "s"
    while repetir != "n":
        barra()
        cabecera()
        print("\nTienes 3 intentos para adivinarlo.\nSin gastar créditos y acumulando puntos.")
        print("\n")
        numero = random.randint(1, 10)
        #print(numero)
        intento = 0
        while intento < 3:
            numero_usu = int(input("¿Qué número crees que estoy pensando? (entre 1-10): "))
            print("\n")
            intento = intento + 1
            if numero == numero_usu:
                print("\nGenial, ese es el número que estaba pensando: ", numero)
                break
            elif numero < numero_usu:
                print("Tu número es demasiado grande.")
            else:
                print("Tu número es demasiado pequeño.")

            if intento < 3:
                print(f"Recuerda, tienes 3 intentos y vas al intento {intento + 1}")
            else:
                cabecera()
                print("No te quedan intentos")
                creditos = creditos - 1
                print(f"{usuario}, esta vez has conseguido {marcador} puntos")

        marca = (3 - intento) * 100
        marcador = marcador + marca
        print(f"En esta partida llevas {marcador} puntos acumulados")
        print(f"Te quedan {creditos} créditos")
        if creditos > 0:
            repetir = input("¿Quieres volver a jugar? s/n ")
            system("cls" )
        else:
            repetir = input("Te has quedado sin créditos. ¿Quieres reiniciar el juego? s/n ")
            if repetir == "s":
                creditos = inicializar_creditos()
                system("cls" )
    return marcador

if __name__ == "__main__":
    cabecera()
    palmares = {"yo Robot":1500}
    creditos = inicializar_creditos()
    usuario = input("Dime tu nombre, por favor: ")
    print(f"Hola, {usuario}, tienes {creditos} créditos.")
    marcador = jugar(creditos, usuario)
    print("Hasta luego")
    print("\n")
    print ("PALMARES")
    nuevo_palmares = ({usuario:marcador})
    palmares.update(nuevo_palmares)
    print(palmares)
    print("\n")


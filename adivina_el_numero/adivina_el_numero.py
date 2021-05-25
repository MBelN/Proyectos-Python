import random

def run():
    numero_random = random.randint(1,100) 
    numero_elegido = int(input("Tenes 5 vidas para adivinar el número! Elegí un número del 1 al 100: "))
    vidas = 5
    while numero_elegido != numero_random:
        if numero_elegido < numero_random:
            if vidas > 1:
                print("")
                print("Buscá un número más grande")
                vidas = vidas - 1
            else:
                print("Te quedaste sin vidas. Perdiste :( el número era " + str(numero_random))
                break
        else:
            if vidas > 1:
                print("")
                print("Buscá un número más pequeño")
                vidas = vidas - 1
            else:
                print("Te quedaste sin vidas. Perdiste :( el número era " + str(numero_random))
                break
        if vidas > 2:
            numero_elegido = int(input("Te quedan " + str(vidas) + " vidas. Elegí otro número: "))
        if vidas == 1:
            numero_elegido = int(input("Te queda " + str(vidas) + " vida. Elegí otro número: "))
    if numero_elegido == numero_random:
        print("Ganaste")


if __name__ == "__main__":
    run()
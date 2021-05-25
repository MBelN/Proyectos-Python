import random
import string

def listAlphabet():
  return list(string.ascii_letters)

def numeros():
    return list(string.digits)


def generar_contrasena():
    letras = listAlphabet()
    simbolos = ["!", "#", "$", "/", "(", ")"]
    lista_numeros = numeros()

    caracteres = letras + simbolos + lista_numeros

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)   #choice para elegir un elemento de la lista caracter
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)                  #para generar un string de la lista
    return contrasena

def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena) 

if __name__ == "__main__":
    run()
import random

def adivina_numero(dificultad):
    if dificultad == "Facil":
        secreto = random.randint(1, 20)
        intentos_maximos = 6
    else:
        secreto = random.randint(1, 100)
        intentos_maximos = 7
    
    intentos_realizados = 0

    while intentos_realizados < intentos_maximos:
        print("Ingresar un número:")
        x = int(input())
        intentos_realizados += 1

        if x == secreto:
            print("bien ahi crack, adivinaste el número secreto:", secreto)
            break
        else:
            if x > secreto:
                print("El número es mayor al secreto")
            else:
                print("El número es menor al secreto")

    if intentos_realizados == intentos_maximos:
        print("Se agotaron los intentos. perdiste pa, El número secreto era:", secreto)


print("que onda, Bienvenido a Adivina el número!")
print("Elige una dificultad: Facil o Dificil")
dificultad_elegida = input().capitalize()

adivina_numero(dificultad_elegida)
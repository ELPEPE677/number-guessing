from random import randint
import time as tm
print("bienvenido al juego de adivina el numero")
while True:
    num_adivinar = randint(1, 100)
    intentos = 0
    intentos_max=0

    dificultad = input("ingresa la dificultad (facil, normal, dificil): ")
    
    while str(dificultad).lower() not in "facil, normal, dificil" or len(dificultad)==0:
        print("debes ingresar una dificultad valida")
        dificultad = input("ingresa la dificultad (facil, normal, dificil): ")
        continue

    if dificultad.lower() == "facil":
        intentos_max = 15
    elif dificultad.lower() == "normal":
        intentos_max = 10
    elif dificultad.lower() == "dificil":
        intentos_max = 5
    print("puedes escribir 'pista' para recibir una pista")


    inicio=tm.time()
    while intentos<=intentos_max:
        print(f"numero de intentos: {intentos}/{intentos_max}")

        num_player = input("adivina un numero entre del 1 al 100: ")

        if str(num_player).lower() == "pista":
            print(f"el numero a adivinar esta entre {num_adivinar-randint(1,10)} y {num_adivinar+randint(1,10)}")
            continue
        try:
            num_player = int(num_player)
        except ValueError:
            print("debes ingresar un numero entero o pista")
            intentos += 1
            continue

        if num_player > 100 or num_player < 1:
            print("debes ingresar un numero entre del 1 al 100")
            intentos += 1
            continue
    
        elif num_player < num_adivinar:
            print("el numero a adivinar es mayor\n")
            intentos+=1
            continue

        elif num_player > num_adivinar:
            print("el numero a adivinar es menor\n")
            intentos+=1
            continue

        else:
            print(f"adivinaste el numero {num_adivinar} en {intentos} intentos")
            break
    if intentos>intentos_max:
        print(f"te pasaste de intentos el numero era {num_adivinar}")

    final=tm.time()
    tiempo=final-inicio
    print(f"tiempo: {tiempo:.2f} segundos")

    continuar=input("quieres continuar s/n: ")

    while continuar.lower() not in "s, n" or len(continuar)==0:
        continuar=input("debes ingresar s o n: ")
        if continuar.lower() == "s":
            break
        elif continuar.lower() == "n":
            break

    if continuar.lower() == "s":
        continue
    elif continuar.lower() == "n":
        break

    
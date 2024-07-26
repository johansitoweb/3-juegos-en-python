import random

def juego_del_ahorcado():
    palabras = ['python', 'programacion', 'desarrollador', 'algoritmo']
    palabra = random.choice(palabras)
    letras_adivinadas = set()
    intentos = 7

    print("Adivina la palabra:")

    while intentos > 0:
        palabra_mostrada = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
        print(palabra_mostrada)
        
        if palabra_mostrada == palabra:
            print("¡Ganaste!")
            break

        letra = input("Introduce una letra: ").lower()
        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra.")
        elif letra in palabra:
            letras_adivinadas.add(letra)
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        if intentos == 0:
            print(f"Perdiste. La palabra era: {palabra}")

juego_del_ahorcado()

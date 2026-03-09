import random
import time

def mostrar_intro():
    print("=== JUEGO: ADIVINA EL NÚMERO ===")
    print("El ordenador pensará un número y tendrás que adivinarlo.")
    print("Cuantos menos intentos uses, más puntos ganarás.")
    print()

def elegir_dificultad():
    print("Selecciona dificultad:")
    print("1 - Fácil (1 a 50)")
    print("2 - Medio (1 a 100)")
    print("3 - Difícil (1 a 200)")
    
    opcion = input("Opción: ")

    if opcion == "1":
        return 50
    elif opcion == "2":
        return 100
    else:
        return 200

def jugar_ronda(limite):
    numero = random.randint(1, limite)
    intentos = 0

    while True:
        try:
            guess = int(input(f"Adivina el número (1-{limite}): "))
            intentos += 1

            if guess < numero:
                print("Demasiado bajo.")
            elif guess > numero:
                print("Demasiado alto.")
            else:
                print(f"¡Correcto! Lo lograste en {intentos} intentos.")
                return intentos

        except ValueError:
            print("Introduce un número válido.")

def calcular_puntos(intentos):
    base = 100
    puntos = max(base - intentos * 10, 10)
    return puntos

def main():
    mostrar_intro()
    limite = elegir_dificultad()

    total_puntos = 0
    rondas = 3
    resultados = []

    for ronda in range(1, rondas + 1):
        print(f"\n--- Ronda {ronda} ---")
        time.sleep(1)

        intentos = jugar_ronda(limite)
        puntos = calcular_puntos(intentos)

        total_puntos += puntos
        resultados.append(intentos)

        print(f"Puntos ganados: {puntos}")

    print("\n=== RESULTADOS ===")
    print("Intentos por ronda:", resultados)
    print("Puntuación total:", total_puntos)

if __name__ == "__main__":
    main()
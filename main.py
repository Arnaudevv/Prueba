import random
import time

def intro():
    titulo = "=== JUEGO: ADIVINA EL NÚMERO ==="
    print(titulo)
    print("El sistema elegirá un número secreto.")
    print("Debes encontrarlo en el menor número de intentos posible.")
    print()

def seleccionar_nivel():
    opciones = {
        "1": 50,
        "2": 100,
        "3": 200
    }

    print("Nivel de dificultad")
    print("1 -> Fácil (1-50)")
    print("2 -> Medio (1-100)")
    print("3 -> Difícil (1-200)")

    eleccion = input("Elige una opción: ")

    return opciones.get(eleccion, 200)

def obtener_numero(limite):
    return random.randint(1, limite)

def pedir_intento(limite):
    while True:
        entrada = input(f"Introduce un número entre 1 y {limite}: ")
        try:
            return int(entrada)
        except:
            print("Entrada inválida.")

def evaluar_intento(numero, intento):
    if intento < numero:
        print("El número es mayor.")
        return False
    elif intento > numero:
        print("El número es menor.")
        return False
    else:
        print("¡Has acertado!")
        return True

def jugar(limite):
    secreto = obtener_numero(limite)
    contador = 0
    encontrado = False

    while not encontrado:
        intento = pedir_intento(limite)
        contador += 1
        encontrado = evaluar_intento(secreto, intento)

    print(f"Intentos utilizados: {contador}")
    return contador

def puntos(intentos):
    puntuacion_base = 100
    penalizacion = intentos * 10
    resultado = puntuacion_base - penalizacion

    if resultado < 10:
        resultado = 10

    return resultado

def juego():
    intro()
    limite = seleccionar_nivel()

    rondas_totales = 3
    historial = []
    puntuacion_total = 0

    for i in range(rondas_totales):
        print(f"\nRonda {i+1}")
        time.sleep(1)

        usados = jugar(limite)
        historial.append(usados)

        score = puntos(usados)
        puntuacion_total += score

        print(f"Puntos obtenidos: {score}")

    print("\n=== RESUMEN FINAL ===")
    print("Intentos por ronda:", historial)
    print("Puntuación final:", puntuacion_total)

if __name__ == "__main__":
    juego()
import random

def obtener_eleccion_valida():
    opciones = ["piedra", "papel", "tijera"]
    while True:
        jugador = input("Elige piedra, papel o tijera: ").lower()
        if jugador in opciones:
            return jugador
        print("Opción no válida. Intenta de nuevo.")

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "empate"
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        return "jugador"
    else:
        return "computadora"

def jugar_mejor_de_tres():
    opciones = ["piedra", "papel", "tijera"]
    puntos_jugador = 0
    puntos_computadora = 0
    rondas = 1

    while puntos_jugador < 2 and puntos_computadora < 2:
        print(f"\n--- Ronda {rondas} ---")
        jugador = obtener_eleccion_valida()
        computadora = random.choice(opciones)
        print(f"Computadora eligió: {computadora}")

        resultado = determinar_ganador(jugador, computadora)
        if resultado == "empate":
            print("¡Empate!")
        elif resultado == "jugador":
            print("¡Ganaste esta ronda!")
            puntos_jugador += 1
        else:
            print("¡Perdiste esta ronda!")
            puntos_computadora += 1

        print(f"Puntuación -> Tú: {puntos_jugador} | Computadora: {puntos_computadora}")
        rondas += 1

    if puntos_jugador > puntos_computadora:
        print("\n🎉 ¡Ganaste la partida! 🎉")
    else:
        print("\n😞 Perdiste la partida. ¡Suerte la próxima!")

# Iniciar el juego
jugar_mejor_de_tres()

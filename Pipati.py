opciones = ['piedra', 'papel', 'tijera']

while True:
    jugador1 = input("Jugador 1 - Elige piedra, papel o tijera (o escribe 'salir'): ").lower()
    if jugador1 == 'salir':
        print("¡Juego terminado!")
        break

    jugador2 = input("Jugador 2 - Elige piedra, papel o tijera: ").lower()

    print(f"\nJugador 1 eligió: {jugador1}")
    print(f"Jugador 2 eligió: {jugador2}")

    if jugador1 == jugador2:
        print("¡Empate!\n")
    elif (jugador1 == 'piedra' and jugador2 == 'tijera') or \
         (jugador1 == 'papel' and jugador2 == 'piedra') or \
         (jugador1 == 'tijera' and jugador2 == 'papel'):
        print("¡Jugador 1 gana!\n")
    else:
        print("¡Jugador 2 gana!\n")
 
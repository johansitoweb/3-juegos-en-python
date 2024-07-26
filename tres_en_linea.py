def imprimir_tablero(tablero):
    for fila in tablero:
        print(' | '.join(fila))
        print('-' * 5)

def es_ganador(tablero, jugador):
    for fila in tablero:
        if all(c == jugador for c in fila):
            return True
    for col in range(3):
        if all(tablero[row][col] == jugador for row in range(3)):
            return True
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)):
        return True
    return False

def tres_en_raya():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugador_actual = 'X'

    for _ in range(9):
        imprimir_tablero(tablero)
        fila = int(input(f"Jugador {jugador_actual}, introduce la fila (0-2): "))
        col = int(input(f"Jugador {jugador_actual}, introduce la columna (0-2): "))
        
        if tablero[fila][col] != ' ':
            print("Ese lugar ya está ocupado. Intenta de nuevo.")
            continue

        tablero[fila][col] = jugador_actual

        if es_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡Jugador {jugador_actual} gana!")
            return

        jugador_actual = 'O' if jugador_actual == 'X' else 'X'

    imprimir_tablero(tablero)
    print("¡Es un empate!")

tres_en_raya()

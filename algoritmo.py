
def busca(tablero, col):
    if tablero.getCelda(0, col) != 0:
        return -1
    i = 0
    while i < tablero.getAlto() and tablero.getCelda(i, col) == 0:
        i += 1
    i -= 1
    return i


def valorHeuristico(tablero):
    # Valor heurístico para el jugador MAX (2)
    valor_max = 0

    # Evaluación en horizontal
    for fila in range(tablero.getAlto()):
        for col in range(tablero.getAncho() - 3):
            ventana = [tablero.getCelda(fila, col + i) for i in range(4)]
            if ventana.count(2) == 4:
                valor_max += 1000
            elif ventana.count(2) == 3 and ventana.count(0) == 1:
                valor_max += 100
            elif ventana.count(2) == 2 and ventana.count(0) == 2:
                valor_max += 10

    # Evaluación en vertical
    for col in range(tablero.getAncho()):
        for fila in range(tablero.getAlto() - 3):
            ventana = [tablero.getCelda(fila + i, col) for i in range(4)]
            if ventana.count(2) == 4:
                valor_max += 1000
            elif ventana.count(2) == 3 and ventana.count(0) == 1:
                valor_max += 100
            elif ventana.count(2) == 2 and ventana.count(0) == 2:
                valor_max += 10

    # Evaluación en diagonal (izquierda a derecha)
    for fila in range(tablero.getAlto() - 3):
        for col in range(tablero.getAncho() - 3):
            ventana = [tablero.getCelda(fila + i, col + i) for i in range(4)]
            if ventana.count(2) == 4:
                valor_max += 1000
            elif ventana.count(2) == 3 and ventana.count(0) == 1:
                valor_max += 100
            elif ventana.count(2) == 2 and ventana.count(0) == 2:
                valor_max += 10

    # Evaluación en diagonal (derecha a izquierda)
    for fila in range(tablero.getAlto() - 3):
        for col in range(3, tablero.getAncho()):
            ventana = [tablero.getCelda(fila + i, col - i) for i in range(4)]
            if ventana.count(2) == 4:
                valor_max += 1000
            elif ventana.count(2) == 3 and ventana.count(0) == 1:
                valor_max += 100
            elif ventana.count(2) == 2 and ventana.count(0) == 2:
                valor_max += 10

    # Valor heurístico para el jugador MIN (1)
    valor_min = 0

    # Evaluación en horizontal
    for fila in range(tablero.getAlto()):
        for col in range(tablero.getAncho() - 3):
            ventana = [tablero.getCelda(fila, col + i) for i in range(4)]
            if ventana.count(1) == 4:
                valor_min += 1000
            elif ventana.count(1) == 3 and ventana.count(0) == 1:
                valor_min += 100
            elif ventana.count(1) == 2 and ventana.count(0) == 2:
                valor_min += 10

    # Evaluación en vertical
    for col in range(tablero.getAncho()):
        for fila in range(tablero.getAlto() - 3):
            ventana = [tablero.getCelda(fila + i, col) for i in range(4)]
            if ventana.count(1) == 4:
                valor_min += 1000
            elif ventana.count(1) == 3 and ventana.count(0) == 1:
                valor_min += 100
            elif ventana.count(1) == 2 and ventana.count(0) == 2:
                valor_min += 10

    # Evaluación en diagonal (izquierda a derecha)
    for fila in range(tablero.getAlto() - 3):
        for col in range(tablero.getAncho() - 3):
            ventana = [tablero.getCelda(fila + i, col + i) for i in range(4)]
            if ventana.count(1) == 4:
                valor_min += 1000
            elif ventana.count(1) == 3 and ventana.count(0) == 1:
                valor_min += 100
            elif ventana.count(1) == 2 and ventana.count(0) == 2:
                valor_min += 10

    # Evaluación en diagonal (derecha a izquierda)
    for fila in range(tablero.getAlto() - 3):
        for col in range(3, tablero.getAncho()):
            ventana = [tablero.getCelda(fila + i, col - i) for i in range(4)]
            if ventana.count(1) == 4:
                valor_min += 1000
            elif ventana.count(1) == 3 and ventana.count(0) == 1:
                valor_min += 100
            elif ventana.count(1) == 2 and ventana.count(0) == 2:
                valor_min += 10

    return valor_max - valor_min


def minimax(tablero, profundidad, alpha, beta, max_player):
    if profundidad == 0 or tablero.cuatroEnRaya() != 0:
        return valorHeuristico(tablero)

    if max_player:
        max_eval = float('-inf')
        best_col = -1
        for col in range(tablero.getAncho()):
            fila = busca(tablero, col)
            if fila != -1:
                tablero.setCelda(fila, col, 2)
                eval = minimax(tablero, profundidad - 1, alpha, beta, False)
                tablero.setCelda(fila, col, 0)
                if eval > max_eval:
                    max_eval = eval
                    best_col = col
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        if profundidad == 4:
            return best_col
        return max_eval
    else:
        min_eval = float('inf')
        for col in range(tablero.getAncho()):
            fila = busca(tablero, col)
            if fila != -1:
                tablero.setCelda(fila, col, 1)
                eval = minimax(tablero, profundidad - 1, alpha, beta, True)
                tablero.setCelda(fila, col, 0)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def alphabeta(tablero, profundidad, alpha, beta, max_player):
    if profundidad == 0 or tablero.cuatroEnRaya() != 0:
        return valorHeuristico(tablero)

    if max_player:
        max_eval = float('-inf')
        best_col = -1
        for col in range(tablero.getAncho()):
            fila = busca(tablero, col)
            if fila != -1:
                tablero.setCelda(fila, col, 2)
                eval = alphabeta(tablero, profundidad - 1, alpha, beta, False)
                tablero.setCelda(fila, col, 0)
                if eval > max_eval:
                    max_eval = eval
                    best_col = col
                alpha = max(alpha, eval)
                if alpha >= beta:
                    break
        if profundidad == 4:
            return best_col
        return max_eval
    else:
        min_eval = float('inf')
        for col in range(tablero.getAncho()):
            fila = busca(tablero, col)
            if fila != -1:
                tablero.setCelda(fila, col, 1)
                eval = alphabeta(tablero, profundidad - 1, alpha, beta, True)
                tablero.setCelda(fila, col, 0)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if alpha >= beta:
                    break
        return min_eval


def juega(tablero, posicion):
    profundidad = 4
    posicion[1] = minimax(tablero, profundidad, float('-inf'), float('inf'), True)
    posicion[0] = busca(tablero, posicion[1])


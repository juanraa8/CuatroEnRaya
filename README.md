# SISTEMAS-INTELIGENTES
Para jugar contra algoritmo alphabeta: 

def juega(tablero, posicion):
    profundidad = 4
    posicion[1] = alphabeta(tablero, profundidad, float('-inf'), float('inf'), True)
    posicion[0] = busca(tablero, posicion[1])

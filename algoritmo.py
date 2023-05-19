# Description: Implementación de algoritmos de búsqueda para el juego Conecta4


# busca en col la primera celda vacía
def busca(tablero, col):  
    if tablero.getCelda(0,col) != 0:
        i=-1
    i=0
    while i<tablero.getAlto() and tablero.getCelda(i,col)==0:          
        i=i+1      
    i=i-1
   
    return i



# encuentra la mejor jugada para la máquina y devuelve la posicion
# para ello implementa un algoritmo minimax con poda alfa-beta

def algoritmominimax(tablero, profundidad, alfa, beta, jugador):
    if tablero.cuatroEnRaya()==1:
        return -1000000
    elif tablero.cuatroEnRaya()==2:
        return 1000000
    elif profundidad==0:
        #return tablero.heuristica()
        return tablero.heuristica()
    elif jugador==1:
        v=-1000000
        for col in range(tablero.getAncho()):
            fila=busca(tablero, col)
            if fila!=-1:
                tablero.setCelda(fila, col, jugador)
                v=max(v, algoritmominimax(tablero, profundidad-1, alfa, beta, 2))
                tablero.setCelda(fila, col, 0)
                alfa=max(alfa, v)
                if beta<=alfa:
                    break
        return v
    else:
        v=1000000
        for col in range(tablero.getAncho()):
            fila=busca(tablero, col)
            if fila!=-1:
                tablero.setCelda(fila, col, jugador)
                v=min(v, algoritmominimax(tablero, profundidad-1, alfa, beta, 1))
                tablero.setCelda(fila, col, 0)
                beta=min(beta, v)
                if beta<=alfa:
                    break
        return v




def juega(tablero, posicion):

    #inicializar variables
    alfa=-1000000
    beta=1000000
    v=-1000000
    col=-1
    profundidad=4
    #para cada columna, calcular la fila y llamar a algoritmominimax
    for c in range(tablero.getAncho()):
        f=busca(tablero, c)
        if f!=-1:
            tablero.setCelda(f, c, 2)
            v2=algoritmominimax(tablero, profundidad-1, alfa, beta, 1)
            if v2>v:
                v=v2
                col=c
            tablero.setCelda(f, c, 0)
    #devolver la columna con el valor más alto
    posicion[0]=busca(tablero, col)
    posicion[1]=col

    #actualizar el array posicion con la fila y columna de la jugada
    return posicion



                
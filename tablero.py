class Tablero:    
    def __init__(self, tabPadre):
        self.ancho=8
        self.alto=7        
        self.tablero=[]
        if tabPadre==None:
            for i in range(self.alto):           
                self.tablero.append([])
                for j in range(self.ancho):
                    self.tablero[i].append(0)
        else:
            for i in range(self.alto):           
                self.tablero.append([])
                for j in range(self.ancho):
                    self.tablero[i].append(tabPadre.getCelda(i,j))          
        
    def __str__(self):
        salida="  0 1 2 3 4 5 6 7\n"
        for f in range(self.alto):
            salida+=str(f)+" "
            for c in range(self.ancho):         
                if self.tablero[f][c] == 0:
                    salida += ". "
                elif self.tablero[f][c] == 1:
                    salida +="1 "
                elif self.tablero[f][c] == 2:
                    salida += "2 "
            salida += "\n"
        return salida
        
                
    def getAncho(self):
        return self.ancho
    
    def getAlto(self):
        return self.alto
    
    def getCelda(self, fila, col):
        return self.tablero[fila][col]
    
    def setCelda(self, fila, col, val):
        self.tablero[fila][col]=val

    # detecta si hay cuatro fichas en línea y devuelve el ganador
    def cuatroEnRaya(self):
        i=0        
        fin=False
        ganador=0
        
        while not fin and i<self.getAlto():
            j=0
            while not fin and j<self.getAncho():
                casilla=self.getCelda(i,j)
                if casilla!=0:
                    #búsqueda en horizontal
                    if (j+3) <self.getAncho():
                        if self.getCelda(i, j+1)==casilla and self.getCelda(i, j+2)==casilla and self.getCelda(i, j+3)==casilla:
                            ganador=casilla
                            fin=True
                    #búsqueda en vertical
                    if (i+3) <self.getAlto():
                        if self.getCelda(i+1, j)==casilla and self.getCelda(i+2, j)==casilla and self.getCelda(i+3, j)==casilla:
                            ganador=casilla
                            fin=True
                    #búsqueda en diagonal
                    if (i+3) <self.getAlto():
                        if (j-3) >= 0:
                            if self.getCelda(i+1, j-1)==casilla and self.getCelda(i+2, j-2)==casilla and self.getCelda(i+3, j-3)==casilla:
                                ganador=casilla
                                fin=True
                        if (j+3) <self.getAncho():
                            if self.getCelda(i+1, j+1)==casilla and self.getCelda(i+2, j+2)==casilla and self.getCelda(i+3, j+3)==casilla:
                                ganador=casilla
                                fin=True
                j=j+1
            i=i+1
        return ganador

    def valorCeldaHorizontal(self, fila, col, ficha):
        #inicializar variables
        valor=0
        #si la celda no está vacía
        if self.getCelda(fila,col)!=0:
            #si la celda es del jugador 1
            if self.getCelda(fila,col)==1:
                #si la celda es del jugador 1
                if ficha==1:
                    #calcular el valor de la celda
                    valor=valor+1
                #si la celda es del jugador 2
                else:
                    #calcular el valor de la celda
                    valor=valor-1
            #si la celda es del jugador 2
            else:
                #si la celda es del jugador 1
                if ficha==1:
                    #calcular el valor de la celda
                    valor=valor-1
                #si la celda es del jugador 2
                else:
                    #calcular el valor de la celda
                    valor=valor+1
        return valor

    def valorCeldaVertical(self, fila, col, ficha):
#inicializar variables
        valor=0
        #si la celda no está vacía
        if self.getCelda(fila,col)!=0:
            #si la celda es del jugador 1
            if self.getCelda(fila,col)==1:
                #si la celda es del jugador 1
                if ficha==1:
                    #calcular el valor de la celda
                    valor=valor+1
                #si la celda es del jugador 2
                else:
                    #calcular el valor de la celda
                    valor=valor-1
            #si la celda es del jugador 2
            else:
                #si la celda es del jugador 1
                if ficha==1:
                    #calcular el valor de la celda
                    valor=valor-1
                #si la celda es del jugador 2
                else:
                    #calcular el valor de la celda
                    valor=valor+1
        return valor

    def valorCeldaDiagonal(self, fila, col, ficha):
#inicializar variables
        valor=0
        #si la celda no está vacía
        if self.getCelda(fila,col)!=0:
            #si la celda es del jugador 1
            if self.getCelda(fila,col)==1:
                #si la celda es del jugador 1
                if ficha==1:
                    #calcular el valor de la celda
                    valor=valor+1
                #si la celda es del jugador 2
                else:
                    #calcular el valor de la celda
                    valor=valor-1
            #si la celda es del jugador 2
            else:
                #si la celda es del jugador 1
                if ficha==1:
                    #calcular el valor de la celda
                    valor=valor-1
                #si la celda es del jugador 2
                else:
                    #calcular el valor de la celda
                    valor=valor+1
        return valor

    #desarrollo de valorCelda
    def valorCelda(self, fila, col, ficha):
        #inicializar variables
        valor=0
        #calcular el valor de la celda
        #calcular el valor de la celda en horizontal
        valor=valor+self.valorCeldaHorizontal(fila, col, ficha)
        #calcular el valor de la celda en vertical
        valor=valor+self.valorCeldaVertical(fila, col, ficha)
        #calcular el valor de la celda en diagonal
        valor=valor+self.valorCeldaDiagonal(fila, col, ficha)
        return valor

    #esto es una prueba de un cambio

   #función de evaluación heuristica de un tablero
    def heuristica(self):
        #inicializar variables
        valor=0
        ficha=1
        #recorrer el tablero
        for i in range(self.getAlto()):
            for j in range(self.getAncho()):
                #calcular el valor de la celda
                valor=valor+self.valorCelda(i, j, ficha)
        return valor






laberinto = []   # Definimos el futuro laberinto como una lista vacia
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))   
        # Creamos las cordenadas de los futuros muros del laberinto
for _ in range (5):
        laberinto.append(([' '])*5)  # Creamos el laberinto sin muros
for i in muro:                                 
        laberinto[int(i[0])][int(i[1])] = 'X'   # De esta manera cada coordenada del                                    
laberinto [4][4] = 'S'                          # muro sera una 'X' en el laberinto
laberinto [0][0] = 'E'   # La primera coordenada del laberinto es una E y la ultima una S
for i in range (5):
        print (laberinto[i])   
        # Printamos de esta manera para obtener saltos de linea

def movimientos ():
        movements = []
        m = 0
        n = 0
        k = 0
        l = 0
        while laberinto[m][n] != 'S':
                if k <= n < 4 and laberinto[m][n+1] != 'X':
                        movements.append("Derecha")
                        n += 1
                        k = n-1
                        l = m
                elif 0 < n < k and laberinto[m][n-1] != 'X':
                        movements.append("Izquierda")
                        n -= 1
                        k = n+1
                        l = n
                elif l <= m < 4 and laberinto[m+1][n] != 'X':
                        movements.append("Abajo")
                        m += 1
                        l = m - 1
                        k = n
                else:
                        movements.append("Arriba")
                        m -= 1
                        l = m + 1
                        k = n
        return movements

print (movimientos())
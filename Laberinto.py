laberinto = []   # Definimos el futuro laberinto como una lista vacia
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))   
# Creamos las cordenadas de los futuros muros del laberinto

def crear_laberinto():
        for _ in range (5):
                laberinto.append(([' '])*5)  # Creamos el laberinto sin muros,
        for i in muro:                                 # con salto de linea incluido
                laberinto[int(i[0])][int(i[1])] = 'X'   # De esta manera cada coordenada del                                    
        return laberinto                                # muro sera una 'X' en el laberinto

ole_ole = crear_laberinto()
print (ole_ole)

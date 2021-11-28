laberinto = []   # Definimos laberinto como una lista vacia
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))   
# Creamos las cordenadas de los futuros muros del laberinto

class tablero:
        def __init__(self):
                for i in range (5):
                        laberinto.append(([' ', ' ', ' ', ' ', ' ']))
                return laberinto
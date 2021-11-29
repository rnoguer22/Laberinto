laberinto = []   # Definimos el futuro laberinto como una lista vacia
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))   
# Creamos las cordenadas de los futuros muros del laberinto

def crear_laberinto():
        for i in range (5):
                laberinto.append(([' '])*5)   # Creamos el laberinto sin muros
        return laberinto


print (laberinto)

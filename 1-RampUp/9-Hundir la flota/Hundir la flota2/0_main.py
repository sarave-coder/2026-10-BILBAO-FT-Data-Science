#Colocar barcos de manera aleatoria

import random
import Variables as var # importar variables creadas para el juego 

# Creación de una clase Tablero
class Tablero:
    def __init__(self, filas=10, columnas=10): # Self:guarda el tablero como una lista de listas
        """Crea un tablero vacío de tamaño filas x columnas."""
        self.AGUA = "|"
        self.BARCO = "B"
        self.filas = filas
        self.columnas = columnas
        self.tablero = [[self.AGUA for _ in range(columnas)] for _ in range(filas)] # Creación de tablero vacío

    def mostrar(self, ocultar_barcos=True): # mostrar los barcos como agua para que el jugador no los vea
        """Muestra el tablero en pantalla."""
        # Columnas
        print("   " + " ".join(str(i) for i in range(self.columnas))) 
        # Filas
        for num_fila, fila in enumerate(self.tablero):
            fila_mostrar = [] # Lista que va guardando lo que va mostrando (agua o barco)
            for celda in fila:
                if ocultar_barcos and celda == self.BARCO:
                    fila_mostrar.append(self.AGUA)
                else:
                    fila_mostrar.append(celda)
            print(f"{num_fila:2} " + " ".join(fila_mostrar)) #Imprimir en número de filas y el contenido
    
# Colocar barcos

    def colocar_barco(self, tamaño):
        """Coloca un barco aleatoriamente en el tablero."""
        colocado = False #Indica si el barco está colocado
        while not colocado: #repite el proceso hasta que el barco se coloque correctamente
            orientacion = random.choice(["X", "Y"])
            fila = random.randint(0, self.filas - 1) #Elige posición aleatoria en el tablero
            col = random.randint(0, self.columnas - 1)

            if orientacion == "X":
                # Comprobar si el baarco cabe y  la posición está libre
                if col + tamaño <= self.columnas and all(self.tablero[fila][c] == self.AGUA for c in range(col, col + tamaño)):
                    for c in range(col, col + tamaño):
                        self.tablero[fila][c] = self.BARCO
                    colocado = True

            else:  # Y
                if fila + tamaño <= self.filas and all(self.tablero[f][col] == self.AGUA for f in range(fila, fila + tamaño)):
                    for f in range(fila, fila + tamaño):
                        self.tablero[f][col] = self.BARCO
                    colocado = True

    def colocar_flota(self, barcos):
        """Coloca todos los barcos definidos en variables.py"""
        for nombre, tamaño, cantidad in var.BARCOS:
            for _ in range(cantidad):
                self.colocar_barco(tamaño)


# Disparar a tableros SEGUIR REVISIÓN AQUÍ

    def disparar(self, fila, col):
        if self.tablero[fila][col] == var.BARCO:
            self.tablero[fila][col] = var.IMPACTO
            print("¡Impacto!")
            return True
        elif self.tablero[fila][col] == var.AGUA:
            self.tablero[fila][col] = var.FALLO
            print("Agua...")
            return False

# Función principal del juego
def juego():
    print("¡Bienvenido a Hundir la Flota!")
    tablero = Tablero()  # Creación del tablero
    tablero.colocar_flota()  # Colocar los barcos
    barcos_restantes = sum(tamaño * cantidad for _, tamaño, cantidad in var.BARCOS)

    # El juego continúa hasta que no queden partes de barcos
    while barcos_restantes > 0:
        tablero.mostrar(ocultar_barcos=not var.MODO_DEBUG)

        try:
            fila = int(input("X: "))
            col = int(input("Y: "))
            if not (0 <= fila < var.TABLERO_FILAS and 0 <= col < var.TABLERO_COLUMNAS):
                print("Coordenadas fuera de rango.")
                continue
            if tablero.disparar(fila, col):
                barcos_restantes -= 1
        except ValueError:
            print("Introduce coordenadas numéricas.")

    # Cuando barcos_restantes llega a 0, el juego termina
    tablero.mostrar(ocultar_barcos=False)
    print("¡Has hundido toda la flota!")
    print("Juego terminado.")

if __name__ == "__main__":
    juego()



#Colocar barcos de manera aleatoria

import random
#crear función barco FALTA

class Barco:

    def __init__(self, eslora): # Inicializa un barco con una longitud (eslora)
        self.eslora = eslora
        self.posiciones = [] # lista de coordenadas donde están

    def colocar(self, tablero): #  Coloca el barco en el tablero de forma aleatoria sin solaparse.
        
        tamaño = len(tablero)
        casillas_totales = tamaño * tamaño
        max_intentos = int((casillas_totales / self.eslora) * 1.5)  #Ajuste de intentos para tablero 10x10
        intentos = 0

        while intentos < max_intentos:
            intentos += 1
            orientacion = random.choice(["X", "Y"]) # X "horizontal" , Y "Vertical"
            fila = random.randint(0, tamaño - 1) # Generar posiciones posibles según orientación
            col = random.randint(0, tamaño - 1)

            if orientacion == "X":
                if col + self.eslora <= tamaño:
                    posiciones_temp = [(fila, c) for c in range(col, col + self.eslora)]
                else:
                    posiciones_temp = []
            else:
                if fila + self.eslora <= tamaño:
                    posiciones_temp = [(f, col) for f in range(fila, fila + self.eslora)]
                else:
                    posiciones_temp = []

           
            if posiciones_temp and all(tablero[f][c] == "~" for f, c in posiciones_temp):  # Verificar que no haya solapamiento
                for f, c in posiciones_temp: #colocar el barco
                    tablero[f][c] = "B"
                self.posiciones = posiciones_temp
                return True #colocado con éxito

        return False #Si no se pudo colocar después de varios intentos
    
    def recibir_disparo(self, fila, col): # Registra un impacto si la posición pertenece al barco.
        if (fila, col) in self.posiciones:
            self.hits += 1
            return True
        return False

    def hundido(self): #Comprueba si el barco está hundido.
        return self.hits == self.eslora


# Crear tableros vacíos 10x10

class Tablero:
    #Tablero jugador 
    tablero_jugador = []
    for i in range(10):
        linea = []
        for j in range(10):
            linea.append(" ")
        tablero_jugador.append(linea)

    tablero_maquina = []
    for i in range(10):
        linea = []
        for j in range(10):
            linea.append(" ")
        tablero_maquina.append(linea)
 
    def colocar_barcos(self):
        barcos_caracteristicas = [
            (4, 1),  # 4 barcos de 1 eslora
            (3, 2),  # 3 barcos de 2 esloras
            (2, 3),  # 2 barcos de 3 esloras
            (1, 4)   # 1 barco de 4 eslora
        ]

        for cantidad, eslora in barcos_caracteristicas:
            for _ in range(cantidad):
                barco = Barco(eslora)
                barco.colocar(self.grid)
                self.barcos.append(barco)

    def mostrar(self, ocultar=False): #Muestra el tablero. Si ocultar=True, no muestra barcos
        for fila in self.grid:
            if ocultar:
                print(" ".join("|" if c == "B" else c for c in fila))
            else:
                print(" ".join(fila))
        print()

    def disparar(self, fila, col): #Realiza un disparo y devuelve si fue acertado
        if not (0 <= fila < self.tamaño and 0 <= col < self.tamaño):
            return "fuera"
        if self.grid[fila][col] in ["X", "O"]:
            return "repetir"

        if self.grid[fila][col] == "B":
            self.grid[fila][col] = "X"
            for barco in self.barcos:
                if barco.recibir_disparo(fila, col) and barco.hundido():
                    return "hundido"
            return "continua"
        else:
            self.grid[fila][col] = "O"
            return "agua"

    def todos_hundidos(self): # Comprueba si todos los barcos están hundidos.
        return all(barco.hundido() for barco in self.barcos)


def turno_jugador(tablero_maquina):
    while True:
        try:
            coords = input("Introduce coordenadas (fila,col): ")
            fila, col = map(int, coords.split(","))
            resultado = tablero_maquina.disparar(fila, col)
            if resultado == "fuera":
                print("Coordenadas fuera del tablero.")
            elif resultado == "repetido":
                print("Ya disparaste ahí.")
            elif resultado == "acierto":
                print("¡Impacto!")
                break
            elif resultado == "hundido":
                print("¡Barco hundido!")
                break
            elif resultado == "agua":
                print("Agua...")
                break
        except ValueError:
            print("Formato inválido. Usa fila,col.")

def turno_maquina(tablero_jugador):
    while True:
        fila = random.randint(0, tablero_jugador.tamaño - 1)
        col = random.randint(0, tablero_jugador.tamaño - 1)
        resultado = tablero_jugador.disparar(fila, col)
        if resultado not in ["repetido", "fuera"]:
            print(f"La máquina dispara a ({fila},{col}) -> {resultado}")
            break

def main():
    tablero_jugador = Tablero()
    tablero_maquina = Tablero()

    tablero_jugador.colocar_barcos()
    tablero_maquina.colocar_barcos()

    print("=== HUNDIR LA FLOTA ===")
    print("Tu tablero:")
    tablero_jugador.mostrar()

    while True:
        print("\nTu turno:")
        tablero_maquina.mostrar(ocultar=True)
        turno_jugador(tablero_maquina)

        if tablero_maquina.todos_hundidos():
            print("¡Has ganado!")
            break

        print("\nTurno de la máquina:")
        turno_maquina(tablero_jugador)
        tablero_jugador.mostrar()

        if tablero_jugador.todos_hundidos():
            print("La máquina ha ganado...")
            break

if __name__ == "__main__":
    main()




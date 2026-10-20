import random 
from variables import * # importar variables creadas para el juego
from clases import * 

# Función principal del juego
def juego():
    print("¡Bienvenido a Hundir la Flota!")
    tablero2 = Tablero()  # Creación del tablero2
    tablero2.colocar_flota(BARCOS)  # Colocar los barcos
    barcos_restantes = sum(tamaño * cantidad for _, tamaño, cantidad in var.BARCOS)

    # El juego continúa hasta que no queden partes de barcos
    while barcos_restantes > 0:
        tablero2.mostrar(ocultar_barcos=not var.MODO_DEBUG)

        try:
            fila = int(input("X: "))
            col = int(input("Y: "))
            if not (0 <= fila < var.TABLERO_FILAS and 0 <= col < var.TABLERO_COLUMNAS):
                print("Coordenadas fuera de rango.")
                continue
            if tablero2.disparar(fila, col):
                barcos_restantes -= 1
        except ValueError:
            print("Introduce coordenadas numéricas.")

    # Cuando barcos_restantes llega a 0, el juego termina
    tablero2.mostrar(ocultar_barcos=False)
    print("¡Has hundido toda la flota!")
    print("Juego terminado.")

if __name__ == "__main__":
    juego()



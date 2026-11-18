from juego import Juego
from menu import Menu


def main():
    """Función principal del programa."""

    print("================================")
    print("       BIENVENIDO AL JUEGO")
    print("================================")

    nombre = input("\nIntroduce tu nombre: ")

    if not nombre.strip():
        nombre = "Jugador"

    print("\nSelecciona la dificultad:")
    print("1. Fácil")
    print("2. Normal")
    print("3. Difícil")

    dificultades = {
        "1": "facil",
        "2": "normal",
        "3": "dificil"
    }

    while True:

        opcion = input("\nElige una dificultad: ")

        if opcion in dificultades:
            dificultad = dificultades[opcion]
            break

        print("Opción no válida. Inténtalo de nuevo.")

    # Crear el juego
    juego = Juego(nombre, dificultad)

    # Crear el menú
    menu = Menu(juego)

    # Iniciar el juego
    menu.ejecutar()


if __name__ == "__main__":
    main()

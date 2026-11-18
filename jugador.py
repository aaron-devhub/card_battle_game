
from carta import Carta
from equipo import Equipo
from personajes import PERSONAJES


class Jugador:

    def __init__(self, nombre):

        self.nombre = nombre

        # Crear las 10 cartas disponibles
        self.cartas_disponibles = []

        for nombre_carta, datos in PERSONAJES.items():

            carta = Carta(
                nombre_carta,
                datos["vida"],
                datos["fuerza"],
                datos["velocidad"],
                datos["defensa"]
            )

            self.cartas_disponibles.append(carta)

        # Crear el equipo del jugador
        self.equipo = Equipo(self.nombre)

    def mostrar_cartas_disponibles(self):
        """Muestra las 10 cartas disponibles."""

        print("\n===== CARTAS DISPONIBLES =====")

        for indice, carta in enumerate(
            self.cartas_disponibles, start=1
        ):

            print(
                f"\n{indice}. {carta.nombre}"
                f"\n   Nivel: {carta.nivel}"
                f"\n   Vida: {carta.vida_maxima}"
                f"\n   Fuerza: {carta.fuerza}"
                f"\n   Velocidad: {carta.velocidad}"
                f"\n   Defensa: {carta.defensa}"
            )

    def seleccionar_cartas(self):
        """Permite seleccionar cinco cartas."""

        self.equipo.limpiar_equipo()

        print("\n===== SELECCIONA TUS 5 CARTAS =====")

        while self.equipo.cantidad_cartas() < Equipo.MAX_CARTAS:

            self.mostrar_cartas_disponibles()

            seleccionadas = self.equipo.cantidad_cartas() + 1

            try:
                opcion = int(input(
                    f"\nSelecciona una carta ({seleccionadas}/5): "
                ))

                if opcion < 1 or opcion > len(self.cartas_disponibles):
                    print("Número de carta no válido.")
                    continue

                carta = self.cartas_disponibles[opcion - 1]

                if self.equipo.agregar_carta(carta):
                    print(f"{carta.nombre} añadida al equipo.")

            except ValueError:
                print("Debes introducir un número.")

        print("\n¡Tu equipo está completo!")

        self.equipo.mostrar_equipo()

    def elegir_carta_combate(self):
        """Permite elegir una carta para combatir."""

        cartas_vivas = self.equipo.obtener_cartas_vivas()

        if not cartas_vivas:
            return None

        print("\n===== ELIGE UNA CARTA PARA COMBATIR =====")

        # Encabezado de la tabla
        print("-" * 100)

        print(
            f"{'Nº':<4}"
            f"{'PERSONAJE':<22}"
            f"{'NIVEL':<9}"
            f"{'VIDA':<13}"
            f"{'FUERZA':<10}"
            f"{'VELOCIDAD':<12}"
            f"{'DEFENSA':<10}"
        )

        print("-" * 100)

        # Mostrar las cartas horizontalmente
        for indice, carta in enumerate(cartas_vivas, start=1):

            print(
                f"{indice:<4}"
                f"{carta.nombre:<22}"
                f"{carta.nivel:<9}"
                f"{str(carta.vida_actual) + '/' + str(carta.vida_maxima):<13}"
                f"{carta.fuerza:<10}"
                f"{carta.velocidad:<12}"
                f"{carta.defensa:<10}"
            )

        print("-" * 100)

        # Seleccionar carta
        while True:

            try:
                opcion = int(input("\nElige tu carta: "))

                if 1 <= opcion <= len(cartas_vivas):
                    return cartas_vivas[opcion - 1]

                print("Selecciona un número válido.")

            except ValueError:
                print("Debes introducir un número.")

    
    def elegir_mejora(self, carta):
        """Permite elegir qué habilidad mejorar respetando sus límites."""

        habilidades = [
            "vida",
            "fuerza",
            "velocidad",
            "defensa"
        ]

        if carta.nivel >= Carta.NIVEL_MAXIMO:
            print(f"{carta.nombre} ya está en nivel máximo.")
            return

        # Filtrar las habilidades que todavía pueden mejorar
        habilidades_disponibles = []

        for habilidad in habilidades:

            if habilidad == "vida":
                valor = carta.vida_maxima
            else:
                valor = getattr(carta, habilidad)

            limite = Carta.LIMITES_HABILIDADES[habilidad]

            if valor < limite:
                habilidades_disponibles.append(habilidad)

        # Comprobar si quedan habilidades disponibles
        if not habilidades_disponibles:
            print(f"{carta.nombre} ya ha alcanzado todos los límites.")
            return

        print(f"\n===== MEJORA DE {carta.nombre} =====")
        print(f"Nivel actual: {carta.nivel}/{Carta.NIVEL_MAXIMO}")

        # Mostrar solamente las habilidades mejorables
        for indice, habilidad in enumerate(habilidades_disponibles, start=1):

            if habilidad == "vida":
                valor = carta.vida_maxima
            else:
                valor = getattr(carta, habilidad)

            limite = Carta.LIMITES_HABILIDADES[habilidad]

            print(
                f"{indice}. {habilidad.capitalize()}: "
                f"{valor}/{limite}"
            )

        # Solicitar elección
        while True:

            try:
                opcion = int(input("\n¿Qué habilidad quieres mejorar? "))

                if 1 <= opcion <= len(habilidades_disponibles):

                    habilidad = habilidades_disponibles[opcion - 1]

                    carta.subir_nivel(habilidad)
                    break

                print("Selecciona una opción válida.")

            except ValueError:
                print("Debes introducir un número.")

    def mostrar_coleccion(self):
        """Muestra todas las cartas y sus niveles."""

        print("\n===== TU COLECCIÓN =====")

        for carta in self.cartas_disponibles:
            carta.mostrar_estadisticas()


import random

from carta import Carta
from equipo import Equipo
from personajes import PERSONAJES


class Maquina:

    DIFICULTADES = ["facil", "normal", "dificil"]

    def __init__(self, dificultad="normal"):

        self.nombre = "Máquina"

        self.dificultad = dificultad.lower()

        if self.dificultad not in self.DIFICULTADES:
            self.dificultad = "normal"

        # Crear las diez cartas independientes
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

        self.equipo = Equipo(self.nombre)

    def cambiar_dificultad(self, dificultad):
        """Cambia la dificultad sin reiniciar las cartas."""

        dificultad = dificultad.lower()

        if dificultad not in self.DIFICULTADES:
            print("Dificultad no válida.")
            return False

        self.dificultad = dificultad

        print(f"Dificultad cambiada a: {self.dificultad}")

        return True

    def seleccionar_cartas(self):
        """Selecciona cinco cartas según la dificultad."""

        self.equipo.limpiar_equipo()

        if self.dificultad == "facil":

            seleccion = self.seleccion_aleatoria()

        elif self.dificultad == "normal":

            seleccion = self.seleccion_equilibrada()

        else:

            seleccion = self.seleccion_estrategica()

        for carta in seleccion:
            self.equipo.agregar_carta(carta)

        print("\nLa máquina ha preparado su equipo.")

    def calcular_puntuacion(self, carta):
        """Calcula una puntuación general normalizada."""

        return (
            carta.vida_maxima * 0.30
            + carta.fuerza * 1.5
            + carta.velocidad * 1.2
            + carta.defensa * 1.5
        )

    def seleccion_aleatoria(self):
        """Selecciona cinco cartas completamente aleatorias."""

        return random.sample(self.cartas_disponibles, 5)

    def seleccion_equilibrada(self):
        """Busca un equipo con estadísticas variadas."""

        cartas = self.cartas_disponibles.copy()

        seleccion = []

        # Añadir una pequeña variación aleatoria
        random.shuffle(cartas)

        while len(seleccion) < Equipo.MAX_CARTAS:

            mejor_carta = None
            mejor_puntuacion = float("-inf")

            for carta in cartas:

                if carta in seleccion:
                    continue

                puntuacion = self.calcular_puntuacion(carta)

                puntuacion += random.uniform(-3, 3)

                if puntuacion > mejor_puntuacion:

                    mejor_puntuacion = puntuacion
                    mejor_carta = carta

            seleccion.append(mejor_carta)

        return seleccion

    def seleccion_estrategica(self):
        """Selecciona cartas con buenas estadísticas generales."""

        cartas = self.cartas_disponibles.copy()

        # Variación para que las elecciones no sean siempre iguales
        random.shuffle(cartas)

        cartas.sort(
            key=lambda carta: (
                self.calcular_puntuacion(carta)
                + random.uniform(-2, 2)
            ),
            reverse=True
        )

        return cartas[:Equipo.MAX_CARTAS]

    def elegir_carta_combate(self):
        """Decide qué carta utilizar en cada enfrentamiento."""

        cartas_vivas = self.equipo.obtener_cartas_vivas()

        if not cartas_vivas:
            return None

        if self.dificultad == "facil":

            return random.choice(cartas_vivas)

        elif self.dificultad == "normal":

            # Combina estrategia y aleatoriedad
            return max(
                cartas_vivas,
                key=lambda carta: (
                    carta.vida_actual * 0.30
                    + carta.fuerza * 1.5
                    + carta.velocidad * 1.2
                    + carta.defensa * 1.5
                    + random.uniform(-5, 5)
                )
            )

        else:

            # La dificultad difícil prioriza cartas con buenas
            # estadísticas y suficiente vida para combatir
            return max(
                cartas_vivas,
                key=lambda carta: (
                    carta.vida_actual * 0.35
                    + carta.fuerza * 1.5
                    + carta.velocidad * 1.5
                    + carta.defensa * 1.5
                )
            )

    def elegir_mejora(self, carta):
        """Decide qué habilidad mejorar respetando sus límites."""

        if carta.nivel >= Carta.NIVEL_MAXIMO:
            print(f"{carta.nombre} ya está en nivel máximo.")
            return False

        # Obtener las habilidades que todavía pueden mejorarse
        habilidades_disponibles = []

        valores = {
            "vida": carta.vida_maxima,
            "fuerza": carta.fuerza,
            "velocidad": carta.velocidad,
            "defensa": carta.defensa
        }

        for habilidad, valor in valores.items():

            limite = Carta.LIMITES_HABILIDADES[habilidad]

            if valor < limite:
                habilidades_disponibles.append(habilidad)

        # Comprobar que queda alguna habilidad por mejorar
        if not habilidades_disponibles:
            print(f"{carta.nombre} no puede mejorar más sus habilidades.")
            return False

        if self.dificultad == "facil":

            habilidad = random.choice(habilidades_disponibles)

        elif self.dificultad == "normal":

            habilidad = random.choice(habilidades_disponibles)

        else:

            # Difícil: elegir la habilidad menos desarrollada
            habilidad = min(
                habilidades_disponibles,
                key=lambda h: valores[h] / Carta.LIMITES_HABILIDADES[h]
            )

        resultado = carta.subir_nivel(habilidad)

        if resultado:
            print(
                f"La máquina ha mejorado "
                f"{carta.nombre}: {habilidad}."
            )

        return resultado

    def mostrar_equipo(self):
        """Muestra el equipo de la máquina."""

        self.equipo.mostrar_equipo()

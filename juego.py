
from jugador import Jugador
from maquina import Maquina
from combate import Combate


class Juego:

    def __init__(self, nombre_jugador, dificultad="normal"):

        self.nombre_jugador = nombre_jugador
        self.dificultad = dificultad

        self.jugador = Jugador(nombre_jugador)
        self.maquina = Maquina(dificultad)

        self.numero_batalla = 1

    def recuperar_vida_cartas(self):
        """Recupera la vida de todas las cartas disponibles."""

        for carta in self.jugador.cartas_disponibles:
            carta.reiniciar_vida()

        for carta in self.maquina.cartas_disponibles:
            carta.reiniciar_vida()

    def preparar_batalla(self):
        """Prepara los equipos para una nueva batalla."""

        print("\n================================")
        print(f"          BATALLA {self.numero_batalla}")
        print("================================")

        # Recuperar la vida al comenzar una nueva batalla
        self.recuperar_vida_cartas()

        # Seleccionar equipos
        self.jugador.seleccionar_cartas()
        self.maquina.seleccionar_cartas()

        print("\n¡Los equipos están preparados!")

    def elegir_cartas(self):
        """Permite elegir las cartas de ambos participantes."""

        print("\n===== SELECCIÓN DE CARTAS =====")

        carta_jugador = self.jugador.elegir_carta_combate()

        carta_maquina = self.maquina.elegir_carta_combate()

        # Comprobar que ambas selecciones son válidas
        if carta_jugador is None or carta_maquina is None:
            return None, None

        print(f"\nTu carta: {carta_jugador.nombre}")

        print(f"Carta de la máquina: {carta_maquina.nombre}")

        return carta_jugador, carta_maquina

    def gestionar_resultado(self, ganador, perdedor):
        """Gestiona las consecuencias de un enfrentamiento."""

        print("\n===== RESULTADO DE LA RONDA =====")

        # Identificar quién ha ganado
        if ganador in self.jugador.equipo.cartas:

            print(f"¡{self.jugador.nombre} ha ganado la ronda!")

            self.jugador.elegir_mejora(ganador)

        elif ganador in self.maquina.equipo.cartas:

            print("¡La máquina ha ganado la ronda!")

            self.maquina.elegir_mejora(ganador)

        else:

            print("Error: no se ha podido identificar al ganador.")
            return False

        # Eliminar al perdedor de su equipo
        if perdedor in self.jugador.equipo.cartas:

            self.jugador.equipo.eliminar_carta(perdedor)

        elif perdedor in self.maquina.equipo.cartas:

            self.maquina.equipo.eliminar_carta(perdedor)

        else:

            print("Error: no se ha podido identificar al perdedor.")
            return False

        print(f"\nCarta eliminada: {perdedor.nombre}")

        return True

    def comprobar_ganador(self):
        """Comprueba si algún equipo se ha quedado sin cartas vivas."""

        jugador_tiene_cartas = self.jugador.equipo.tiene_cartas()

        maquina_tiene_cartas = self.maquina.equipo.tiene_cartas()

        if not jugador_tiene_cartas and not maquina_tiene_cartas:

            print("\n¡La batalla ha terminado en empate!")
            return "empate"

        if not jugador_tiene_cartas:

            print("\n¡LA MÁQUINA HA GANADO LA BATALLA!")

            return self.maquina

        if not maquina_tiene_cartas:

            print(f"\n¡{self.jugador.nombre} HA GANADO LA BATALLA!")

            return self.jugador

        return None

    def mostrar_estado(self):
        """Muestra el estado actual de los equipos."""

        print("\n========== ESTADO DE LOS EQUIPOS ==========")

        self.jugador.equipo.mostrar_equipo()

        self.maquina.equipo.mostrar_equipo()

    def ejecutar_ronda(self, ronda):
        """Ejecuta un enfrentamiento entre dos cartas."""

        print(f"\n========== RONDA {ronda} ==========")

        # Seleccionar cartas
        carta_jugador, carta_maquina = self.elegir_cartas()

        if carta_jugador is None or carta_maquina is None:
            print("No se puede continuar con el enfrentamiento.")
            return False

        # Crear y ejecutar el combate
        combate = Combate(carta_jugador, carta_maquina)

        ganador = combate.ejecutar()

        if ganador is None:
            print("No se ha podido determinar el ganador.")
            return False

        # Identificar al perdedor
        if ganador is carta_jugador:
            perdedor = carta_maquina
        else:
            perdedor = carta_jugador

        # Gestionar las consecuencias
        resultado = self.gestionar_resultado(ganador, perdedor)

        if not resultado:
            return False

        # Mostrar estado de los equipos
        self.mostrar_estado()

        return True

    def jugar_batalla(self):
        """Controla todas las rondas de una batalla."""

        self.preparar_batalla()

        ronda = 1

        while True:

            # Comprobar si alguien ha perdido antes de empezar
            ganador_batalla = self.comprobar_ganador()

            if ganador_batalla is not None:
                break

            # Ejecutar una ronda
            resultado = self.ejecutar_ronda(ronda)

            if not resultado:
                print("\nLa batalla se ha interrumpido.")
                return None

            # Comprobar el resultado de la batalla
            ganador_batalla = self.comprobar_ganador()

            if ganador_batalla is not None:
                break

            ronda += 1

        print("\n========== BATALLA FINALIZADA ==========")

        self.numero_batalla += 1

        return ganador_batalla

    def reiniciar_juego(self):
        """Reinicia las cartas y sus niveles."""

        self.jugador = Jugador(self.nombre_jugador)

        self.maquina = Maquina(self.dificultad)

        self.numero_batalla = 1

        print("\n================================")
        print("       JUEGO REINICIADO")
        print("================================")

        print("Todas las cartas vuelven al nivel 1.")

    def mostrar_coleccion(self):
        """Muestra la colección completa del jugador."""

        self.jugador.mostrar_coleccion()

from jugador import Jugador
from maquina import Maquina
from combate import Combate


class Juego:

    def __init__(self, nombre_jugador, dificultad="normal"):

        self.nombre_jugador = nombre_jugador
        self.dificultad = dificultad

        self.jugador = Jugador(nombre_jugador)
        self.maquina = Maquina(dificultad)

        self.numero_batalla = 1

    def recuperar_vida_cartas(self):
        """Recupera la vida de todas las cartas disponibles."""

        for carta in self.jugador.cartas_disponibles:
            carta.reiniciar_vida()

        for carta in self.maquina.cartas_disponibles:
            carta.reiniciar_vida()

    def preparar_batalla(self):
        """Prepara los equipos para una nueva batalla."""

        print("\n================================")
        print(f"          BATALLA {self.numero_batalla}")
        print("================================")

        # Recuperar la vida al comenzar una nueva batalla
        self.recuperar_vida_cartas()

        # Seleccionar equipos
        self.jugador.seleccionar_cartas()
        self.maquina.seleccionar_cartas()

        print("\n¡Los equipos están preparados!")

    def elegir_cartas(self):
        """Permite elegir las cartas de ambos participantes."""

        print("\n===== SELECCIÓN DE CARTAS =====")

        carta_jugador = self.jugador.elegir_carta_combate()

        carta_maquina = self.maquina.elegir_carta_combate()

        # Comprobar que ambas selecciones son válidas
        if carta_jugador is None or carta_maquina is None:
            return None, None

        print(f"\nTu carta: {carta_jugador.nombre}")

        print(f"Carta de la máquina: {carta_maquina.nombre}")

        return carta_jugador, carta_maquina

    def gestionar_resultado(self, ganador, perdedor):
        """Gestiona las consecuencias de un enfrentamiento."""

        print("\n===== RESULTADO DE LA RONDA =====")

        # Identificar quién ha ganado
        if ganador in self.jugador.equipo.cartas:

            print(f"¡{self.jugador.nombre} ha ganado la ronda!")

            self.jugador.elegir_mejora(ganador)

        elif ganador in self.maquina.equipo.cartas:

            print("¡La máquina ha ganado la ronda!")

            self.maquina.elegir_mejora(ganador)

        else:

            print("Error: no se ha podido identificar al ganador.")
            return False

        # Eliminar al perdedor de su equipo
        if perdedor in self.jugador.equipo.cartas:

            self.jugador.equipo.eliminar_carta(perdedor)

        elif perdedor in self.maquina.equipo.cartas:

            self.maquina.equipo.eliminar_carta(perdedor)

        else:

            print("Error: no se ha podido identificar al perdedor.")
            return False

        print(f"\nCarta eliminada: {perdedor.nombre}")

        return True

    def comprobar_ganador(self):
        """Comprueba si algún equipo se ha quedado sin cartas vivas."""

        jugador_tiene_cartas = self.jugador.equipo.tiene_cartas()

        maquina_tiene_cartas = self.maquina.equipo.tiene_cartas()

        if not jugador_tiene_cartas and not maquina_tiene_cartas:

            print("\n¡La batalla ha terminado en empate!")
            return "empate"

        if not jugador_tiene_cartas:

            print("\n¡LA MÁQUINA HA GANADO LA BATALLA!")

            return self.maquina

        if not maquina_tiene_cartas:

            print(f"\n¡{self.jugador.nombre} HA GANADO LA BATALLA!")

            return self.jugador

        return None

    def mostrar_estado(self):
        """Muestra el estado actual de los equipos."""

        print("\n========== ESTADO DE LOS EQUIPOS ==========")

        self.jugador.equipo.mostrar_equipo()

        self.maquina.equipo.mostrar_equipo()

    def ejecutar_ronda(self, ronda):
        """Ejecuta un enfrentamiento entre dos cartas."""

        print(f"\n========== RONDA {ronda} ==========")

        # Seleccionar cartas
        carta_jugador, carta_maquina = self.elegir_cartas()

        if carta_jugador is None or carta_maquina is None:
            print("No se puede continuar con el enfrentamiento.")
            return False

        # Crear y ejecutar el combate
        combate = Combate(carta_jugador, carta_maquina)

        ganador = combate.ejecutar()

        if ganador is None:
            print("No se ha podido determinar el ganador.")
            return False

        # Identificar al perdedor
        if ganador is carta_jugador:
            perdedor = carta_maquina
        else:
            perdedor = carta_jugador

        # Gestionar las consecuencias
        resultado = self.gestionar_resultado(ganador, perdedor)

        if not resultado:
            return False

        # Mostrar estado de los equipos
        self.mostrar_estado()

        return True

    def jugar_batalla(self):
        """Controla todas las rondas de una batalla."""

        self.preparar_batalla()

        ronda = 1

        while True:

            # Comprobar si alguien ha perdido antes de empezar
            ganador_batalla = self.comprobar_ganador()

            if ganador_batalla is not None:
                break

            # Ejecutar una ronda
            resultado = self.ejecutar_ronda(ronda)

            if not resultado:
                print("\nLa batalla se ha interrumpido.")
                return None

            # Comprobar el resultado de la batalla
            ganador_batalla = self.comprobar_ganador()

            if ganador_batalla is not None:
                break

            ronda += 1

        print("\n========== BATALLA FINALIZADA ==========")

        self.numero_batalla += 1

        return ganador_batalla

    def reiniciar_juego(self):
        """Reinicia las cartas y sus niveles."""

        self.jugador = Jugador(self.nombre_jugador)

        self.maquina = Maquina(self.dificultad)

        self.numero_batalla = 1

        print("\n================================")
        print("       JUEGO REINICIADO")
        print("================================")

        print("Todas las cartas vuelven al nivel 1.")

    def mostrar_coleccion(self):
        """Muestra la colección completa del jugador."""

        self.jugador.mostrar_coleccion()

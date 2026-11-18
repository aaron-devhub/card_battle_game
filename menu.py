
class Menu:

    def __init__(self, juego):

        self.juego = juego
        self.ejecutando = True

    def mostrar_menu_principal(self):
        """Muestra las opciones principales."""

        print("\n================================")
        print("          JUEGO DE CARTAS")
        print("================================")
        print("1. Jugar batalla")
        print("2. Consultar colección")
        print("3. Cambiar dificultad")
        print("4. Reiniciar juego")
        print("5. Salir")
        print("================================")

    def mostrar_menu_final(self, ganador):
        """Muestra las opciones después de una batalla."""

        print("\n================================")
        print("          FIN DE BATALLA")
        print("================================")

        if ganador == "empate":
            print("Resultado: EMPATE")

        elif ganador == self.juego.jugador:
            print("¡HAS GANADO LA BATALLA!")

        elif ganador == self.juego.maquina:
            print("LA MÁQUINA HA GANADO.")

        else:
            print("La batalla no ha finalizado correctamente.")

        print("\n¿Qué quieres hacer?")
        print("1. Volver a seleccionar cartas y jugar")
        print("2. Consultar colección")
        print("3. Reiniciar juego")
        print("4. Cambiar dificultad")
        print("5. Volver al menú principal")
        print("6. Salir")

    def consultar_coleccion(self):
        """Muestra todas las cartas del jugador."""

        self.juego.mostrar_coleccion()

        self.pausa()

    def cambiar_dificultad(self):
        """Permite cambiar la dificultad de la máquina."""

        print("\n========== DIFICULTAD ==========")
        print("1. Fácil")
        print("2. Normal")
        print("3. Difícil")

        opciones = {
            "1": "facil",
            "2": "normal",
            "3": "dificil"
        }

        opcion = input("\nSelecciona la dificultad: ").strip()

        if opcion in opciones:

            dificultad = opciones[opcion]

            resultado = self.juego.maquina.cambiar_dificultad(
                dificultad
            )

            if resultado:
                self.juego.dificultad = dificultad

        else:

            print("\nOpción no válida.")

    def confirmar_reinicio(self):
        """Solicita confirmación antes de reiniciar."""

        respuesta = input(
            "\n¿Seguro que quieres reiniciar? "
            "Perderás todos los niveles obtenidos (s/n): "
        ).strip().lower()

        if respuesta == "s":

            self.juego.reiniciar_juego()

            return True

        elif respuesta == "n":

            print("\nReinicio cancelado.")

            return False

        else:

            print("\nRespuesta no válida.")

            return False

    def pausa(self):
        """Espera hasta que el usuario pulse ENTER."""

        input("\nPulsa ENTER para continuar...")

    def ejecutar(self):
        """Controla el menú principal."""

        while self.ejecutando:

            self.mostrar_menu_principal()

            opcion = input("\nSelecciona una opción: ").strip()

            if opcion == "1":

                ganador = self.juego.jugar_batalla()

                if ganador is not None:
                    self.menu_despues_batalla(ganador)

            elif opcion == "2":

                self.consultar_coleccion()

            elif opcion == "3":

                self.cambiar_dificultad()

            elif opcion == "4":

                self.confirmar_reinicio()

            elif opcion == "5":

                print("\n¡Gracias por jugar!")

                self.ejecutando = False

            else:

                print("\nOpción no válida. Inténtalo de nuevo.")

    def menu_despues_batalla(self, ganador):
        """Gestiona las opciones al finalizar una batalla."""

        while self.ejecutando:

            self.mostrar_menu_final(ganador)

            opcion = input("\nSelecciona una opción: ").strip()

            if opcion == "1":

                # Conservar los niveles y comenzar otra batalla
                return

            elif opcion == "2":

                self.consultar_coleccion()

            elif opcion == "3":

                self.confirmar_reinicio()

                # Volver al menú principal
                return

            elif opcion == "4":

                self.cambiar_dificultad()

            elif opcion == "5":

                # Volver al menú principal
                return

            elif opcion == "6":

                print("\n¡Gracias por jugar!")

                self.ejecutando = False

                return

            else:

                print("\nOpción no válida. Inténtalo de nuevo.")

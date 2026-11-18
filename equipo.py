
class Equipo:

    MAX_CARTAS = 5

    def __init__(self, nombre):

        self.nombre = nombre
        self.cartas = []

    def agregar_carta(self, carta):
        """Añade una carta al equipo."""

        # Comprobar que no se ha alcanzado el límite
        if len(self.cartas) >= self.MAX_CARTAS:
            print("El equipo ya tiene 5 cartas.")
            return False

        # Evitar cartas duplicadas
        if carta in self.cartas:
            print("Esta carta ya está en el equipo.")
            return False

        # Evitar dos personajes con el mismo nombre
        if any(c.nombre == carta.nombre for c in self.cartas):
            print("Esta carta ya está en el equipo.")
            return False

        self.cartas.append(carta)

        return True

    def eliminar_carta(self, carta):
        """Elimina una carta concreta del equipo."""

        if carta in self.cartas:

            self.cartas.remove(carta)

            return True

        return False

    def obtener_cartas_vivas(self):
        """Devuelve únicamente las cartas que siguen vivas."""

        return [
            carta for carta in self.cartas
            if carta.esta_viva()
        ]

    def tiene_cartas(self):
        """Comprueba si quedan cartas vivas en el equipo."""

        return len(self.obtener_cartas_vivas()) > 0

    def cantidad_cartas(self):
        """Devuelve el número total de cartas del equipo."""

        return len(self.cartas)

    def cantidad_cartas_vivas(self):
        """Devuelve el número de cartas que siguen vivas."""

        return len(self.obtener_cartas_vivas())

    def mostrar_equipo(self):
        """Muestra todas las cartas del equipo."""

        print(f"\n========== {self.nombre} ==========")

        if not self.cartas:
            print("El equipo no tiene cartas.")
            return

        for indice, carta in enumerate(self.cartas, start=1):

            estado = "Viva" if carta.esta_viva() else "Derrotada"

            print(
                f"{indice}. {carta.nombre} "
                f"| Nivel: {carta.nivel} "
                f"| Vida: {carta.vida_actual}/{carta.vida_maxima} "
                f"| Estado: {estado}"
            )

        print(
            f"\nCartas vivas: {self.cantidad_cartas_vivas()}"
            f"/{self.cantidad_cartas()}"
        )

    def limpiar_equipo(self):
        """Vacía completamente el equipo."""

        self.cartas.clear()

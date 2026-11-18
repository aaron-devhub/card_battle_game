
class Carta:

    NIVEL_MAXIMO = 20
    NIVEL_MAXIMO = 20

    HABILIDADES = ["vida", "fuerza", "velocidad", "defensa"]

    LIMITES_HABILIDADES = {
        "vida": 60,
        "fuerza": 20,
        "velocidad": 15,
        "defensa": 15
    }

    def __init__(self, nombre, vida, fuerza, velocidad, defensa):

        # Identidad
        self.nombre = nombre

        # Nivel
        self.nivel = 1

        # Estadísticas iniciales
        self.vida_maxima = vida
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.defensa = defensa

        # Vida durante el combate
        self.vida_actual = vida

    def recibir_danio(self, danio):
        """Reduce la vida de la carta según el daño recibido."""

        # No recibir daño si ya está derrotada
        if not self.esta_viva():
            return 0

        # El daño nunca puede ser inferior a 1
        danio_real = max(1, danio - self.defensa)

        # Evitar que la vida sea negativa
        danio_aplicado = min(self.vida_actual, danio_real)

        self.vida_actual -= danio_aplicado

        return danio_aplicado

    def esta_viva(self):
        """Comprueba si la carta sigue viva."""

        return self.vida_actual > 0

    def reiniciar_vida(self):
        """Recupera toda la vida de la carta."""

        self.vida_actual = self.vida_maxima

    def subir_nivel(self, habilidad):
        """Aumenta una habilidad respetando sus límites."""

        if self.nivel >= self.NIVEL_MAXIMO:
            print(f"{self.nombre} ya ha alcanzado el nivel máximo.")
            return False

        if habilidad not in self.LIMITES_HABILIDADES:
            print("Habilidad no válida.")
            return False

        # Obtener el valor actual de la habilidad
        if habilidad == "vida":
            valor_actual = self.vida_maxima
        else:
            valor_actual = getattr(self, habilidad)

        # Obtener el límite de la habilidad
        limite = self.LIMITES_HABILIDADES[habilidad]

        # Comprobar si ha alcanzado el límite
        if valor_actual >= limite:
            print(f"{habilidad.capitalize()} ya está al máximo ({limite}).")
            return False

        # Mejorar habilidad
        if habilidad == "vida":
            self.vida_maxima += 1
            self.vida_actual = min(
                self.vida_maxima,
                self.vida_actual + 1
            )

        else:
            setattr(self, habilidad, valor_actual + 1)

        self.nivel += 1

        print(f"\n¡{self.nombre} ha subido al nivel {self.nivel}!")
        print(f"{habilidad.capitalize()}: {valor_actual} -> {valor_actual + 1}")

        return True

    def mostrar_estadisticas(self):
        """Muestra las estadísticas de la carta."""

        print(f"\n========== {self.nombre} ==========")

        print(f"Nivel: {self.nivel}/{self.NIVEL_MAXIMO}")

        print(
            f"Vida: {self.vida_actual}/{self.vida_maxima}"
        )

        print(f"Fuerza: {self.fuerza}")
        print(f"Velocidad: {self.velocidad}")
        print(f"Defensa: {self.defensa}")

        print("=================================")

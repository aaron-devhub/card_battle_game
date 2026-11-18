
import random


class Combate:

    PROBABILIDAD_CRITICO = 0.15
    MULTIPLICADOR_CRITICO = 1.5 
    PROBABILIDAD_ESQUIVA_BASE = 0.10
    PROBABILIDAD_ESQUIVA_MINIMA = 0.05
    PROBABILIDAD_ESQUIVA_MAXIMA = 0.30
    BONIFICACION_VELOCIDAD = 0.03

    def __init__(self, carta_jugador, carta_maquina):

        self.carta_jugador = carta_jugador
        self.carta_maquina = carta_maquina

        self.turno = 1

    def calcular_probabilidad_esquivar(self, defensor, atacante):
        """Calcula la probabilidad de esquivar según la velocidad."""

        diferencia = defensor.velocidad - atacante.velocidad

        probabilidad = (
            self.PROBABILIDAD_ESQUIVA_BASE
            + diferencia * self.BONIFICACION_VELOCIDAD
        )

        return max(
            self.PROBABILIDAD_ESQUIVA_MINIMA,
            min(self.PROBABILIDAD_ESQUIVA_MAXIMA, probabilidad)
        )

    def atacar(self, atacante, defensor):
        """Ejecuta un ataque con posibilidad de golpe crítico."""

        print(f"\n{atacante.nombre} ataca a {defensor.nombre}.")

        # Comprobar si el defensor esquiva
        probabilidad = self.calcular_probabilidad_esquivar(
            defensor, atacante
        )

        if random.random() < probabilidad:

            print(f"¡{defensor.nombre} ha esquivado el ataque!")
            return

        # Calcular daño base
        variacion = random.randint(-1, 2)

        danio = max(1, atacante.fuerza + variacion)

        # Comprobar golpe crítico
        critico = random.random() < self.PROBABILIDAD_CRITICO

        if critico:

            danio = int(danio * self.MULTIPLICADOR_CRITICO)

            print("\n¡¡¡ GOLPE CRÍTICO !!!")

        # Aplicar daño
        vida_anterior = defensor.vida_actual

        defensor.recibir_danio(danio)

        danio_real = vida_anterior - defensor.vida_actual

        print(f"Daño causado: {danio_real}")

        print(
            f"Vida de {defensor.nombre}: "
            f"{defensor.vida_actual}/{defensor.vida_maxima}"
        )

        if not defensor.esta_viva():

            print(f"¡{defensor.nombre} ha sido derrotado!")
            
    def determinar_primer_atacante(self):
        """Determina quién comienza atacando."""

        if self.carta_jugador.velocidad > self.carta_maquina.velocidad:

            return self.carta_jugador, self.carta_maquina

        elif self.carta_maquina.velocidad > self.carta_jugador.velocidad:

            return self.carta_maquina, self.carta_jugador

        # Si tienen la misma velocidad, se decide aleatoriamente
        return tuple(
            random.sample(
                [self.carta_jugador, self.carta_maquina],
                2
            )
        )

    def mostrar_resultado(self, ganador, perdedor):
        """Muestra el resultado del enfrentamiento."""

        print("\n========== FIN DEL COMBATE ==========")

        print(f"Ganador: {ganador.nombre}")

        print(f"Perdedor: {perdedor.nombre}")

        print(
            f"Vida restante del ganador: "
            f"{ganador.vida_actual}/{ganador.vida_maxima}"
        )

        print("=====================================")

    def ejecutar(self):
        """Gestiona el combate completo entre dos cartas."""

        # Comprobar que ambas cartas pueden combatir
        if (
            not self.carta_jugador.esta_viva()
            or not self.carta_maquina.esta_viva()
        ):

            print("No se puede iniciar el combate.")

            return None

        print("\n========== COMIENZA EL COMBATE ==========")

        print(
            f"\n{self.carta_jugador.nombre} "
            f"VS {self.carta_maquina.nombre}"
        )

        print(
            f"\n{self.carta_jugador.nombre}: "
            f"{self.carta_jugador.vida_actual} PV"
        )

        print(
            f"{self.carta_maquina.nombre}: "
            f"{self.carta_maquina.vida_actual} PV"
        )

        # Determinar quién comienza
        atacante, defensor = self.determinar_primer_atacante()

        print(f"\n{atacante.nombre} comienza atacando.")

        # Combate por turnos
        while (
            self.carta_jugador.esta_viva()
            and self.carta_maquina.esta_viva()
        ):

            print(f"\n---------- TURNO {self.turno} ----------")

            self.atacar(atacante, defensor)

            # Comprobar si el defensor ha sido derrotado
            if not defensor.esta_viva():
                break

            # Intercambiar atacante y defensor
            atacante, defensor = defensor, atacante

            self.turno += 1

        # Determinar ganador y perdedor
        if self.carta_jugador.esta_viva():

            ganador = self.carta_jugador
            perdedor = self.carta_maquina

        else:

            ganador = self.carta_maquina
            perdedor = self.carta_jugador

        self.mostrar_resultado(ganador, perdedor)

        return ganador

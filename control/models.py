from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import json
import random
import string

author = 'Steffanny Romero'

doc = """
Experimento para tesis de maestría / grupo de control
"""


class Constants(BaseConstants):
    name_in_url = 'control'
    players_per_group = 6
    num_rounds = 3
    piecerateSC = c(1000)
    piecerateC = c(960)
    bonusC = c(160)
    bonusSC = c(120)
    letters_per_word = 5
    use_timeout = True
    seconds_per_period = 10
    # use_word_target = 

class Subsession(BaseSubsession):
    def creating_session(self):
            for p in self.get_players():
                ronda_pagar = random.randint(2, Constants.num_rounds)
                p.task_pay = ronda_pagar

class Group(BaseGroup):

    total_performance=models.IntegerField(initial=0)
    jugadores_C = models.IntegerField()
    jugadores_SC = models.IntegerField()
    pago_promedio_C = models.CurrencyField(initial=c(0))
    pago_promedio_SC = models.CurrencyField(initial=c(0))

    def set_total_performance(self):
        for jugador in self.get_players():
            if jugador.market == 'C':
                self.total_performance += jugador.palabras

    def set_payoffs(self):
        for jugador in self.get_players():
            if jugador.market == 'C':
                jugador.payoff = (Constants.piecerateC*jugador.palabras)+ Constants.bonusC*self.total_performance
                self.pago_promedio_C += jugador.payoff
            else:
                jugador.payoff = (Constants.piecerateSC*jugador.palabras)+ Constants.bonusSC*self.total_performance
                self.pago_promedio_SC += jugador.payoff
        if self.jugadores_C != 0:
            self.pago_promedio_C /= self.jugadores_C
        else:
            self.pago_promedio_C = 0
        if self.jugadores_SC != 0:
            self.pago_promedio_SC /= self.jugadores_SC
        else:
            self.pago_promedio_SC = 0

    def set_jugador_C(self):
        contador = 0
        for jugador in self.get_players():
            if jugador.market == 'C':
                contador += 1
        self.jugadores_C = contador

    def set_jugador_SC(self):
        contador = 0
        for jugador in self.get_players():
            if jugador.market == 'SC':
                contador += 1
        self.jugadores_SC = contador

class Player(BasePlayer):
    task_pay = models.IntegerField()
    palabras = models.IntegerField(initial=0)
    mistakes = models.IntegerField(initial=0)
    filtro = models.IntegerField()
    identificador = models.StringField(label='Para iniciar por favor ingrese las iniciales de su primer nombre y apellido seguido de su fecha de nacimiento. Por ejemplo, si usted se llama Lina Ríos y usted nació el 11 de febrero de 1995, debe ingresar LR11021995. Escriba todo en mayúscula. Esta etiqueta es importante para asegurar su participación en el resto de la actividad y la realización de los pagos.')
    consent = models.BooleanField(blank=True)
    consent_account = models.BooleanField(blank=True)

    market = models.StringField(
        choices=[['C', 'Mercado C (con contribución): Mis tareas completadas dan un beneficio a los demás miembros del grupo, y yo me beneficio de las tareas completadas por los miembros del grupo que escojan este mercado.'], ['SC', 'Mercado SC (sin contribución): Me beneficio de las tareas completadas por los miembros del grupo que escojan el Mercado C, y mis tareas completadas me dan un beneficio más alto que en el mercado C, pero sólo a mí.']],
        label='Por favor seleccione el mercado en el que desea participar esta ronda:',
        widget=widgets.RadioSelectHorizontal(),
    )

    belief = models.IntegerField(
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
        label="Recuerde que usted está en un grupo de 6 personas. De las otras 5 personas ¿Cuántas cree que seleccionaron el Mercado C (con contribución)?",
        widget=widgets.RadioSelectHorizontal(),
    )

    c_1 = models.IntegerField(
        choices=[[1, 'Mis tareas completadas dan un beneficio a los demás miembros del grupo, y yo me beneficio de las tareas completadas por los miembros del grupo que escojan este mercado.'], [0, 'Mis tareas completadas no dan un beneficio a los demás miembros del grupo, y yo me beneficio de las tareas completadas por los miembros del grupo que escojan este mercado.']],
        label='1. Por favor seleccione la respuesta que corresponde al Mercado C (con contribución):',
        widget=widgets.RadioSelect,
    )
    c_2 = models.IntegerField(
        choices=[[0, 'No me beneficio de las tareas completadas por los miembros del grupo que escojan el Mercado C, y mis tareas completadas me dan un beneficio más alto que en el mercado C, pero sólo a mí.'], [1, 'Me beneficio de las tareas completadas por los miembros del grupo que escojan el Mercado C, y mis tareas completadas me dan un beneficio más alto que en el mercado C, pero sólo a mí.']],
        label='2. Por favor seleccione la respuesta que corresponde al Mercado SC (sin contribución):',
        widget=widgets.RadioSelect,
    )

    p1 = models.IntegerField(
        choices=[[1, 'Hombre'], [2, 'Mujer'], [3, 'No binario']], label="1. ¿Con qué género se identifica?", widget=widgets.RadioSelectHorizontal(),)

    p2 = models.IntegerField(label="2. Edad (Escriba únicamente números")
    p3 = models.IntegerField(
    choices=[
        [1,'Estudiante'],
        [2,'Desempleado'],
        [3,'Empleado a jornada completa'],
        [4,'Empleado a tiempo parcial'],
        [5,'Trabajador independiente'],
        [6,'Trabajador no remunerado (por ejemplo: ama de casa, empresa familiar)'],
        [7,'Retirado/pensionado'],
        [8,'Otro'],
        [9,'No sabe']
    ], label="3. ¿Cuál es su situación laboral actual?")
    p4 = models.StringField(label="4. Escriba el nombre de su profesión/ocupación")
    p5 = models.IntegerField(
    choices=[
        [1,'Ninguno'],
        [2,'Primaria incompleta'],
        [3,'Bachillerato'],
        [4,'Técnico o Tecnólogo'],
        [5,'Pregrado'],
        [6,'Posgrado (Especialización, Maestría, Doctorado)']
    ], label="5. ¿Cuál es el nivel educativo más alto que ha completado?")
    p6 = models.IntegerField(
    choices=[
        [1,'Subsidiado'],
        [2,'Contributivo (incluye regímenes especiales)']
    ], label="6. A qué régimen de seguridad social en salud pertenece", widget=widgets.RadioSelectHorizontal(),
    )

    p7_1 = models.PositiveIntegerField(choices=[1,2,3,4],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Gobierno"
                                       )
    p7_2 = models.PositiveIntegerField(choices=[1,2,3,4],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Ministerio de Salud y Protección Social"
                                       )
    p7_3 = models.PositiveIntegerField(choices=[1,2,3,4],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Administradora de los Recursos del Sistema General de Seguridad Social en Salud -ADRES-"
                                       )
    p7_4 = models.PositiveIntegerField(choices=[1,2,3,4],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Administradora Colombiana de Pensiones -Colpensiones-"
                                       )
    p8_1 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Ayudar a otras personas me da mucha felicidad"
                                       )
    p8_2 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="No tengo una gran sensación de felicidad cuando actúo desinteresadamente"
                                       )
    p8_3 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Cada vez que tuve la oportunidad de ayudar a otros, me sentí muy bien después"
                                       )
    p8_4 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Ayudar a otras personas a las que no les va bien no mejora mi estado de ánimo"
                                       )
    p8_5 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="No siento que tenga que realizar actos altruistas hacia los demás"
                                       )
    p8_6 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="No considero que mi deber sea actuar desinteresadamente"
                                       )
    p8_7 = models.PositiveIntegerField(choices=[1,2,3,4,5],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Siento el deber de ayudar a los demás siempre que sea posible para mí"
                                       )

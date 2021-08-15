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

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'questions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass
class Player(BasePlayer):
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

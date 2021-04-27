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
    name_in_url = 'information'
    players_per_group = 6
    num_rounds = 5
    piecerateSC = c(1000)
    piecerateC = c(960)
    bonusC = c(160)
    bonusSC = c(120)
    letters_per_word = 5

    use_timeout = True
    seconds_per_period = 10
    seconds_try = 60

class Subsession(BaseSubsession):
    dictionary = models.StringField()
    def creating_session(self):
        # Create dictionary
        letters = list(string.ascii_uppercase)
        random.shuffle(letters)
        numbers = []
        N = list(range(100, 1000))
        for i in range(27):
            choice = random.choice(N)
            N.remove(choice)
            numbers.append(choice)
        d = [letters, numbers]
        dictionary = dict([(d[0][i], d[1][i]) for i in range(26)])
        self.dictionary = json.dumps(dictionary)


class Group(BaseGroup):

    total_performance=models.IntegerField(initial=0)
    jugadores_C = models.IntegerField()
    jugadores_SC = models.IntegerField()
    pago_promedio_C = models.CurrencyField(initial=c(0))
    pago_promedio_SC = models.CurrencyField(initial=c(0))

    def set_total_performance(self):
        for jugador in self.get_players():
            self.total_performance = self.total_performance + jugador.performance1

    def set_payoffs(self):
        for jugador in self.get_players():
            if jugador.market == 'C':
                jugador.payoff = (Constants.piecerateC*jugador.performance1)+ Constants.bonusC*self.total_performance
                self.pago_promedio_C += jugador.payoff
            else:
                jugador.payoff = (Constants.piecerateSC*jugador.performance1)+ Constants.bonusSC*self.total_performance
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

    performance = models.IntegerField(initial=0)
    mistakes = models.IntegerField(initial=0)
    performance1 = models.IntegerField(initial=0)
    mistakes1 = models.IntegerField(initial=0)
    tarea1= models.IntegerField()
    tarea2 = models.IntegerField()
    filtro = models.IntegerField()

    market = models.StringField(
        choices=[['C', 'Mercado C (con contribución)'], ['SC', 'Mercado SC (sin contribución)']],
        label='Por favor seleccione el mercado en el que desea participar esta ronda:',
        widget=widgets.RadioSelect,
    )

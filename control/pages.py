from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class consent(Page):
    form_model = 'player'
    form_fields = ['consent','consent_account']

    def is_displayed(self):
        return self.round_number == 1

class Initial(Page):
    form_model = 'player'
    form_fields = ['identificador']

    def is_displayed(self):
        if(self.round_number == 1):
            return True
        else:
            return False

    def before_next_page(self):
        self.participant.vars['identificador'] = self.player.identificador


class instrucciones(Page):
    def is_displayed(self):
        return self.round_number == 1


class choice(Page):
    def is_displayed(self):
        return self.round_number > 1

    form_model = 'player'
    form_fields = ['market']

    def vars_for_template(self):
        return {
                "ronda": self.round_number - 1,
                }


class check(Page):
    def is_displayed(self):
        return self.round_number == 2

    form_model = 'player'
    form_fields = ['c_1', 'c_2']


class belief(Page):
    def is_displayed(self):
        return self.round_number > 1

    form_model = 'player'
    form_fields = ['belief']


class tarea(Page):
    def is_displayed(self):
        return self.round_number > 0

    form_model = 'player'
    form_fields = ['palabras', 'mistakes']
    if Constants.use_timeout:
        timeout_seconds = Constants.seconds_per_period

    def vars_for_template(self):
        legend_list = [j for j in range(5)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90 / Constants.letters_per_word
        return {'legend_list': legend_list,
                'task_list': task_list,
                'task_width': task_width,
                "ronda": self.round_number - 1,
                }


class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number > 1

    def after_all_players_arrive(self):
        self.group.set_total_performance() # CAlcule el desempeño del grupo una vez ermino todo el grupo
        self.group.set_jugador_C()
        self.group.set_jugador_SC()
        self.group.set_payoffs()

class Results(Page):
    def is_displayed(self):
        if(self.round_number > 1):
            if(self.group.jugadores_C):
                marketC_without_self = self.group.jugadores_C if self.player.market != 'C' else self.group.jugadores_C - 1
                self.player.win_belief = True if marketC_without_self == self.player.belief else False
        if (self.round_number == Constants.num_rounds):
            pays = []
            for rj in (self.player.in_all_rounds()):
                pays.append(format(int(str(rj.payoff).split(",")[0]),',d'))
            self.participant.vars['pays'] = pays
            self.participant.vars['payoff'] = self.player.in_round(self.player.task_pay).payoff
            self.participant.vars['win'] = self.player.in_round(self.player.task_pay).win_belief

        return self.round_number > 1

    def vars_for_template(self):
        return {
            'palabras': self.player.palabras,
            'ronda': self.round_number - 1,
            'jug_C': self.group.jugadores_C,
            'jug_SC': self.group.jugadores_SC,
            "prom_C":  "$"+format(int(str(self.group.pago_promedio_C).split(",")[0]),',d'),
            "prom_SC":  "$"+format(int(str(self.group.pago_promedio_SC).split(",")[0]),',d'),
            "pay_player":  "$"+format(int(str(self.player.payoff).split(",")[0]),',d'),

        }


class pago_total(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'codigo': self.player.in_round(1).identificador,
            'ronda_pagar': self.player.task_pay - 1,
            'pago_completo': format(int(str(self.player.in_round(self.player.task_pay).payoff).split(",")[0]),',d')
        }


class Instructions2(Page):
    def is_displayed(self):
        return self.round_number > 1

    def vars_for_template(self):
        return {
            'jug_market': self.player.market,
            "ronda": self.round_number - 1,
        }


class Markets(Page):
    def is_displayed(self):
        return self.round_number == 2


class questions(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    form_model = 'player'
    form_fields = ['p1',
                   'p2',
                   'p3',
                   'p4',
                   'p5',
                   'p6',
                   'p7_1',
                   'p7_2',
                   'p7_3',
                   'p7_4',
                   'p8_3',
                   'p8_4',
                   'p8_6',
                   'p8_7']


page_sequence = [consent,
                 Initial,
                 instrucciones,
                 Markets,
                 check,
                 choice,
                 belief,
                 Instructions2,
	             tarea,
                 ResultsWaitPage,
                 Results]
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Initial(Page):
    def is_displayed(self):
        if(self.round_number == 1):
            return True
        else:
            return False

class Task2(Page):
    form_model = 'player'
    form_fields = ['performance1', 'mistakes1']
    if Constants.use_timeout:
        timeout_seconds = Constants.seconds_per_period

    def vars_for_template(self):
        legend_list = [j for j in range(5)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90/Constants.letters_per_word
        return{'legend_list': legend_list,
               'task_list': task_list,
               'task_width': task_width}

class Try(Page):
    form_model = 'player'
    form_fields = ['performance', 'mistakes']
    timeout_seconds = 10

    def is_displayed(self):
        if(self.round_number == 1):
            return True
        else:
            return False

    def vars_for_template(self):
        legend_list = [j for j in range(5)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90/Constants.letters_per_word
        return{'legend_list': legend_list,
               'task_list': task_list,
               'task_width': task_width}

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_total_performance() # CAlcule el desempeño del grupo una vez ermino todo el grupo
        self.group.set_jugador_C()
        self.group.set_jugador_SC()
        self.group.set_payoffs()

class Results(Page):
    def vars_for_template(self):
        self.player.tarea2 = self.player.performance1
        return {
            'performance': self.player.tarea2,
            'jug_C': self.group.jugadores_C,
            'jug_SC': self.group.jugadores_SC,
            'prom_C': self.group.pago_promedio_C,
            'prom_SC':self.group.pago_promedio_SC
        }

class Instructions(Page):
    def is_displayed(self):
        if(self.round_number == 1):
            return True
        else:
            return False

class Instructions2(Page):
    def vars_for_template(self):
        return {
            'jug_market': self.player.market,
        }

class Markets(Page):
    form_model = 'player'
    form_fields = ['market']

page_sequence = [Initial,
                 Instructions,
                 Try,
                 Markets,
                 Instructions2,
                 Task2,
                 ResultsWaitPage,
                 Results]

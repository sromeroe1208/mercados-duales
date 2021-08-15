from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class pago_total(Page):
    
    def vars_for_template(self):
        print('vars is', self.participant.vars)
        return {
            'codigo': self.participant.vars['identificador'],
            'ronda_pagar': self.participant.vars['task_pay'] - 1,
            'pago_completo': format(int(str(self.participant.vars['payoff']).split(",")[0]),',d'),
            'win_belief':  self.participant.vars['win'],
            'pays': self.participant.vars['pays']
        }



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
                   'p8_1',
                   'p8_2',
                   'p8_3',
                   'p8_4',
                   'p8_5',
                   'p8_6',
                   'p8_7']


page_sequence = [
                 questions,
                 pago_total,
                 ]

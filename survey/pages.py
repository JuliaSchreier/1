from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Pairs(Page):
    def vars_for_template(self):
      return self.player.vars_for_template()

    form_model = 'player'
    form_fields = ['pair_answer', 'pair_answer_mask', "pair_answer_mean"]

class Five_scarce(Page):
	def vars_for_template(self):
		return self.player.vars_for_template()

	form_model = 'player'
	form_fields = ['five_scarce', 'five_scarce_answer_mask', 'five_scarce_answer_mean']

class Multiple_choice(Page):
	def vars_for_template(self):
		return self.player.vars_for_template()

	form_model = 'player'
	form_fields = ["five_mc", "five_mc_mean1", "five_mc_mean2","five_mc_mean3","five_mc_mean4","five_mc_mean5"]

class Lottery1_1(Page):
	def vars_for_template(self):
		return self.player.vars_for_template()

	form_model = 'player'
	form_fields = ['lottery1_1']

class Lottery1_2(Page):
	def vars_for_template(self):
		return self.player.vars_for_template()

	form_model = 'player'
	form_fields = ['lottery1_2', "lottery1_player", "lottery1_mask", "lottery1_value"]

class Lottery1_3(Page):
	def vars_for_template(self):
		return self.player.vars_for_template()

	form_model = 'player'
	form_fields = ['lottery1_3', "lottery1_player", "lottery1_mask", "lottery1_value"]

class Lottery1_4(Page):
	def vars_for_template(self):
		return self.player.vars_for_template()

	form_model = 'player'
	form_fields = ['lottery1_4', "lottery1_player", "lottery1_mask", "lottery1_value"]

class Lottery1_5(Page):
	def vars_for_template(self):
		return self.player.vars_for_template()

	form_model = 'player'
	form_fields = ['lottery1_5', "lottery1_player", "lottery1_mask", "lottery1_value"]

class Endowment(Page):
	def vars_for_template(self):
		return self.player.vars_for_template()

	form_model = 'player'

class Start(Page):
	form_model = 'player'

class End(Page):
	def vars_for_template(self):
		return self.player.vars_for_template()

	form_model = 'player'

class End2(Page):
	def vars_for_template(self):
		return self.player.vars_for_template()

	form_model = 'player'


# class Age(Page):
# 	def vars_for_template(self):
# 		return self.player.vars_for_template()

# 	form_model = 'player'
# 	form_fields = ['age']

page_sequence = [
	Start,
    Endowment,
    Pairs,
    Five_scarce, 
    Multiple_choice,
    Lottery1_1,
    Lottery1_2,
    Lottery1_3,
    Lottery1_4,
    Lottery1_5,
    End,
    End2
]
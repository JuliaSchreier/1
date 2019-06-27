from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from otree_tools.models import fields as tool_models
import random
import numpy as np
import pandas as pd


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1
    mask_values = {'masks': ['', 'mask1.png', 'mask2.png', 'mask3.png', 'mask4.png', 'mask5.png', 'mask6.png', 'mask7.png', 'mask8.png', 'mask9.png', 'mask10.png', 'mask11.png', 'mask12.png', 'mask13.png', 'mask14.png', 'mask15.png', 'mask16.png', 'mask17.png', 'mask18.png', 'mask19.png', 'mask20.png', 'mask21.png', 'mask22.png', 'mask23.png', 'mask24.png', 'mask25.png', 'mask26.png', 'mask27.png', 'mask28.png', 'mask29.png', 'mask30.png', 'mask31.png', 'mask32.png', 'mask33.png', 'mask34.png', 'mask35.png', 'mask36.png', 'mask37.png', 'mask38.png', 'mask39.png', 'mask40.png', 'mask41.png', 'mask42.png', 'mask43.png', 'mask44.png', 'mask45.png', 'mask46.png', 'mask47.png', 'mask48.png', 'mask49.png', 'mask50.png', 'mask51.png', 'mask52.png', 'mask53.png', 'mask54.png', 'mask55.png', 'mask56.png', 'mask57.png', 'mask58.png', 'mask59.png', 'mask60.png', 'mask61.png', 'mask62.png', 'mask63.png', 'mask64.png', 'mask65.png', 'mask66.png', 'mask67.png', 'mask68.png', 'mask69.png', 'mask70.png', 'mask71.png', 'mask72.png', 'mask73.png', 'mask74.png', 'mask75.png', 'mask76.png', 'mask77.png', 'mask78.png', 'mask79.png', 'mask80.png', 'mask81.png', 'mask82.png', 'mask83.png', 'mask84.png', 'mask85.png', 'mask86.png', 'mask87.png', 'mask88.png', 'mask89.png', 'mask90.png', 'mask91.png', 'mask92.png', 'mask93.png', 'mask94.png', 'mask95.png', 'mask96.png', 'mask97.png', 'mask98.png', 'mask99.png', 
    'mask1info.png', 'mask2info.png', 'mask3info.png', 'mask4info.png', 'mask5info.png', 'mask6info.png',
     'mask7info.png', 'mask8info.png', 'mask9info.png', 'mask10info.png', 'mask11info.png', 'mask12info.png', 'mask13info.png', 
     'mask14info.png', 'mask15info.png', 'mask16info.png', 'mask17info.png', 'mask18info.png', 'mask19info.png', 'mask20info.png', 
     'mask21info.png', 'mask22info.png', 'mask23info.png', 'mask24info.png', 'mask25info.png', 'mask26info.png', 'mask27info.png', 
     'mask28info.png', 'mask29info.png', 'mask30info.png', 'mask31info.png', 'mask32info.png', 'mask33info.png', 'mask34info.png', 
     'mask35info.png', 'mask36info.png', 'mask37info.png', 'mask38info.png', 'mask39info.png', 'mask40info.png', 'mask41info.png',
      'mask42info.png', 'mask43info.png', 'mask44info.png', 'mask45info.png', 'mask46info.png', 'mask47info.png', 'mask48info.png',
       'mask49info.png', 'mask50info.png', 'mask51info.png', 'mask52info.png', 'mask53info.png', 'mask54info.png', 'mask55info.png', 
       'mask56info.png', 'mask57info.png', 'mask58info.png', 'mask59info.png', 'mask60info.png', 'mask61info.png', 'mask62info.png', 
       'mask63info.png', 'mask64info.png', 'mask65info.png', 'mask66info.png', 'mask67info.png', 'mask68info.png', 'mask69info.png', 
       'mask70info.png', 'mask71info.png', 'mask72info.png', 'mask73info.png', 'mask74info.png', 'mask75info.png', 'mask76info.png', 
       'mask77info.png', 'mask78info.png', 'mask79info.png', 'mask80info.png', 'mask81info.png', 'mask82info.png', 'mask83info.png', 
       'mask84info.png', 'mask85info.png', 'mask86info.png', 'mask87info.png', 'mask88info.png', 'mask89info.png', 'mask90info.png',
        'mask91info.png', 'mask92info.png', 'mask93info.png', 'mask94info.png', 'mask95info.png', 'mask96info.png', 'mask97info.png', 
        'mask98info.png', 'mask99info.png'], 
    'mean': [None, 75.25, 77.0, 78.75, 72.0, 73.75, 75.5, 71.75, 70.25, 73.5, 71.25, 71.25, 74.75, 75.75, 75.75, 73.75, 75.75, 76.5, 72.25, 73.5, 78.75, 67.75, 74.5, 74.25, 71.5, 78.5, 71.0, 71.5, 71.75, 73.75, 77.75, 77.75, 79.25, 75.75, 72.75, 70.0, 72.5, 75.0, 74.25, 80.75, 68.75, 73.0, 71.25, 71.0, 73.25, 76.0, 71.75, 74.5, 79.0, 73.25, 72.0, 80.25, 72.5, 76.75, 71.0, 73.75, 75.5, 76.5, 72.5, 78.0, 76.0, 69.75, 78.0, 73.0, 74.75, 72.25, 76.5, 72.75, 75.0, 71.75, 77.5, 72.75, 75.5, 83.0, 75.75, 71.75, 69.5, 76.75, 72.5, 71.75, 74.5, 78.0, 74.25, 75.0, 73.75, 77.75, 69.75, 75.0, 73.5, 77.25, 73.75, 76.25, 72.75, 73.0, 71.25, 72.5, 76.5, 77.0, 75.25, 74.25,
    74.16666666666667, 75.16666666666667, 75.16666666666667, 80.66666666666667, 76.5, 73.0, 76.83333333333333, 74.66666666666667, 72.0, 74.83333333333333, 73.66666666666667, 72.66666666666667, 75.16666666666667, 73.0, 76.33333333333333, 74.33333333333333, 75.83333333333333, 73.5, 74.83333333333333, 75.66666666666667, 75.16666666666667, 78.83333333333333, 73.5, 77.0, 76.0, 73.0, 73.16666666666667, 75.0, 73.16666666666667, 73.5, 77.0, 75.0, 75.0, 76.0, 79.33333333333333, 73.33333333333333, 74.66666666666667, 73.33333333333333, 72.0, 75.16666666666667, 68.5, 75.0, 73.5, 75.83333333333333, 75.5, 75.5, 78.83333333333333, 75.33333333333333, 74.83333333333333, 74.16666666666667, 72.66666666666667, 73.16666666666667, 74.66666666666667, 74.66666666666667, 75.0, 76.33333333333333, 75.16666666666667, 75.0, 75.66666666666667, 75.83333333333333, 72.16666666666667, 73.66666666666667, 73.66666666666667, 73.16666666666667, 73.83333333333333, 74.66666666666667, 75.0, 74.83333333333333, 76.0, 76.16666666666667, 73.33333333333333, 73.5, 75.0, 74.33333333333333, 72.66666666666667, 74.33333333333333, 75.5, 77.16666666666667, 75.5, 72.83333333333333, 72.16666666666667, 72.66666666666667, 75.66666666666667, 73.83333333333333, 71.5, 77.83333333333333, 78.0, 74.33333333333333, 74.66666666666667, 70.5, 78.5, 73.5, 74.16666666666667, 74.33333333333333, 72.33333333333333, 72.66666666666667, 74.66666666666667, 78.5, 75.66666666666667],}
    df_masks = pd.DataFrame(mask_values)
    

from .widgets import ImageCheckboxSelectMultiple

class Subsession(BaseSubsession):
	def creating_session(self):
		for player in self.get_players():

			###### Information treatment
			player.full_information = random.choice([True, False])

			###### Probability treatment
			player.probability = random.choice([True, False]) 

			###### Player Setup
			# list including all names of players 
			playerlist = ["babel.png", "holland.png", "mueller.png", "kefkir.png", "sanogo.png", 
			"sabiri.png", "ryan.png", "sabiri.png", "öztürk.png", "oezbiliz.png", "neagle.png", 
			"mannek.png", "maak.png", "hartherz.png", "hermannsson.png", "hardeveldt.png", 
			"gülen.png", "geisler.png", "edmundsson.png", "clarke.png", "canouse.png", "bahoui.png",
			"bouhaddouz.png", "ayhan.png", "ayhan2.png", "ayaz.png"]
			
			# shuffle player list to randomize position in list
			random.shuffle(playerlist)

			##### Masks Setup 
			# list all possible masks for combination
			if player.full_information == False: 
				masks = ['mask1.png', 'mask2.png', 'mask3.png', 'mask4.png', 'mask5.png', 'mask6.png', 'mask7.png', 
				'mask8.png', 'mask9.png', 'mask10.png', 'mask11.png', 'mask12.png', 'mask13.png', 'mask14.png', 'mask15.png', 
				'mask16.png', 'mask17.png', 'mask18.png', 'mask19.png', 'mask20.png', 'mask21.png', 'mask22.png', 'mask23.png', 
				'mask24.png', 'mask25.png', 'mask26.png', 'mask27.png', 'mask28.png', 'mask29.png', 'mask30.png', 'mask31.png', 
				'mask32.png', 'mask33.png', 'mask34.png', 'mask35.png', 'mask36.png', 'mask37.png', 'mask38.png', 'mask39.png', 
				'mask40.png', 'mask41.png', 'mask42.png', 'mask43.png', 'mask44.png', 'mask45.png', 'mask46.png', 'mask47.png', 
				'mask48.png', 'mask49.png', 'mask50.png', 'mask51.png', 'mask52.png', 'mask53.png', 'mask54.png', 'mask55.png', 
				'mask56.png', 'mask57.png', 'mask58.png', 'mask59.png', 'mask60.png', 'mask61.png', 'mask62.png', 'mask63.png', 
				'mask64.png', 'mask65.png', 'mask66.png', 'mask67.png', 'mask68.png', 'mask69.png', 'mask70.png', 'mask71.png', 
				'mask72.png', 'mask73.png', 'mask74.png', 'mask75.png', 'mask76.png', 'mask77.png', 'mask78.png', 'mask79.png', 
				'mask80.png', 'mask81.png', 'mask82.png', 'mask83.png', 'mask84.png', 'mask85.png', 'mask86.png', 'mask87.png', 
				'mask88.png', 'mask89.png', 'mask90.png', 'mask91.png', 'mask92.png', 'mask93.png', 'mask94.png', 'mask95.png', 
				'mask96.png', 'mask97.png', 'mask98.png', 'mask99.png']

			if player.full_information == True:
				masks = ['mask1info.png', 'mask2info.png', 'mask3info.png', 'mask4info.png', 'mask5info.png', 'mask6info.png',
				'mask7info.png', 'mask8info.png', 'mask9info.png', 'mask10info.png', 'mask11info.png', 'mask12info.png', 'mask13info.png', 
				'mask14info.png', 'mask15info.png', 'mask16info.png', 'mask17info.png', 'mask18info.png', 'mask19info.png', 'mask20info.png', 
				'mask21info.png', 'mask22info.png', 'mask23info.png', 'mask24info.png', 'mask25info.png', 'mask26info.png', 'mask27info.png', 
				'mask28info.png', 'mask29info.png', 'mask30info.png', 'mask31info.png', 'mask32info.png', 'mask33info.png', 'mask34info.png', 
				'mask35info.png', 'mask36info.png', 'mask37info.png', 'mask38info.png', 'mask39info.png', 'mask40info.png', 'mask41info.png',
				'mask42info.png', 'mask43info.png', 'mask44info.png', 'mask45info.png', 'mask46info.png', 'mask47info.png', 'mask48info.png',
				'mask49info.png', 'mask50info.png', 'mask51info.png', 'mask52info.png', 'mask53info.png', 'mask54info.png', 'mask55info.png', 
				'mask56info.png', 'mask57info.png', 'mask58info.png', 'mask59info.png', 'mask60info.png', 'mask61info.png', 'mask62info.png', 
				'mask63info.png', 'mask64info.png', 'mask65info.png', 'mask66info.png', 'mask67info.png', 'mask68info.png', 'mask69info.png', 
				'mask70info.png', 'mask71info.png', 'mask72info.png', 'mask73info.png', 'mask74info.png', 'mask75info.png', 'mask76info.png', 
				'mask77info.png', 'mask78info.png', 'mask79info.png', 'mask80info.png', 'mask81info.png', 'mask82info.png', 'mask83info.png', 
				'mask84info.png', 'mask85info.png', 'mask86info.png', 'mask87info.png', 'mask88info.png', 'mask89info.png', 'mask90info.png',
				'mask91info.png', 'mask92info.png', 'mask93info.png', 'mask94info.png', 'mask95info.png', 'mask96info.png', 'mask97info.png', 
				'mask98info.png', 'mask99info.png']

			# shuffle masks
			random.shuffle(masks)

			###### Endowment 
			player.endowment = random.choice(['low', 'medium', 'high'])

			##### Endowment 
			if player.endowment == 'low':
				player.endowment1mask = masks[17]
				player.endowment2mask = masks[18]
				player.endowment3mask = masks[19]
				player.endowment4mask = masks[20]

			if player.endowment == 'medium':
				player.endowment1mask = masks[17]
				player.endowment2mask = masks[18]
				player.endowment3mask = masks[19]
				player.endowment4mask = masks[20]

			if player.endowment == 'high':
				player.endowment1mask = masks[17]
				player.endowment2mask = masks[18]
				player.endowment3mask = masks[19]
				player.endowment4mask = masks[20]


			player.endowment1value =  Constants.df_masks.loc[Constants.df_masks['masks'] == player.endowment1mask, ['mean']].values
			player.endowment2value =  Constants.df_masks.loc[Constants.df_masks['masks'] == player.endowment2mask, ['mean']].values
			player.endowment3value =  Constants.df_masks.loc[Constants.df_masks['masks'] == player.endowment3mask, ['mean']].values
			player.endowment4value =  Constants.df_masks.loc[Constants.df_masks['masks'] == player.endowment4mask, ['mean']].values
			
			##### First Pair
			# use position in list for random placement in games
			player.pairs1_1 = playerlist[0] # Pair 1/ left 
			player.pairs1_2 = playerlist[1] # Pair 1/ right
			
			# use position 
			player.mask1_1 = masks[0]
			player.mask1_2 = masks[1]

			# mask value
			player.mask1_1_value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.mask1_1, ['mean']].values
			player.mask1_2_value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.mask1_2, ['mean']].values

			###### 1 out of 5 (five_scarce)
			player.five_scarce1 = playerlist[2]
			player.five_scarce2 = playerlist[3]
			player.five_scarce3 = playerlist[4]
			player.five_scarce4 = playerlist[5]
			player.five_scarce5 = playerlist[6]

			player.five_mask1 = masks[2]
			player.five_mask2 = masks[3]
			player.five_mask3 = masks[4]
			player.five_mask4 = masks[5]
			player.five_mask5 = masks[6]

			# mask value
			player.five_mask1_value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.five_mask1, ['mean']].values
			player.five_mask2_value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.five_mask2, ['mean']].values
			player.five_mask3_value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.five_mask3, ['mean']].values
			player.five_mask4_value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.five_mask4, ['mean']].values
			player.five_mask5_value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.five_mask5, ['mean']].values

			###### 3 out of 5 (five_multiple)
			player.five_multiple1 = playerlist[7]
			player.five_multiple2 = playerlist[8]
			player.five_multiple3 = playerlist[9]
			player.five_multiple4 = playerlist[10]
			player.five_multiple5 = playerlist[11]

			player.five_m_mask1 = masks[7]
			player.five_m_mask2 = masks[8]
			player.five_m_mask3 = masks[9]
			player.five_m_mask4 = masks[10]
			player.five_m_mask5 = masks[11]

			player.five_m_mask1value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.five_m_mask1, ['mean']].values
			player.five_m_mask2value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.five_m_mask2, ['mean']].values
			player.five_m_mask3value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.five_m_mask3, ['mean']].values
			player.five_m_mask4value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.five_m_mask4, ['mean']].values
			player.five_m_mask5value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.five_m_mask5, ['mean']].values

			####### Lottery 1 ##########
			player.lottery1_1_img = playerlist[12]
			player.lottery1_2_img = playerlist[13]
			player.lottery1_3_img = playerlist[14]
			player.lottery1_4_img = playerlist[15]
			player.lottery1_5_img = playerlist[16]

			player.lottery1_1_mask = masks[12]
			player.lottery1_2_mask = masks[13]
			player.lottery1_3_mask = masks[14]
			player.lottery1_4_mask = masks[15]
			player.lottery1_5_mask = masks[16]

			player.lottery1_1_value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.lottery1_1_mask, ['mean']].values
			player.lottery1_2_value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.lottery1_2_mask, ['mean']].values
			player.lottery1_3_value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.lottery1_3_mask, ['mean']].values
			player.lottery1_4_value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.lottery1_4_mask, ['mean']].values
			player.lottery1_5_value = Constants.df_masks.loc[Constants.df_masks['masks'] == player.lottery1_5_mask, ['mean']].values


			player.endowment1 = playerlist[17]
			player.endowment2 = playerlist[18]
			player.endowment3 = playerlist[19]
			player.endowment4 = playerlist[20]

			#player.team_endowment_list = list(filter(None, [player.endowment1value, player.endowment2value, player.endowment3value, player.endowment4value, player.five_scarce_answer_mean]))

class Group(BaseGroup):
    pass



class Player(BasePlayer):
	from .widgets import ImageCheckboxSelectMultiple

	# Full information 
	full_information = models.BooleanField()

	# Probability
	probability = models.BooleanField()

	# Endowment
	endowment = models.StringField()

	#team_endowment_list = tool_models.ListField()
	
	
	# endowment
	endowment1 = models.StringField()
	endowment2 = models.StringField()
	endowment3 = models.StringField()
	endowment4 = models.StringField()

	endowment1mask = models.StringField()
	endowment2mask = models.StringField()
	endowment3mask = models.StringField()
	endowment4mask = models.StringField()

	endowment1value = models.IntegerField()
	endowment2value = models.IntegerField()
	endowment3value = models.IntegerField()
	endowment4value = models.IntegerField()

	#### First Pair 
	# Player on left 
	pairs1_1 = models.StringField()
	# Stats on left 
	mask1_1 = models.StringField()

	# player on right
	pairs1_2 = models.StringField()
	# Stats on right
	mask1_2 = models.StringField()

	# mask values
	mask1_1_value = models.IntegerField()
	mask1_2_value = models.IntegerField()

	# empty field for value
	pair_answer = models.StringField()
	pair_answer_mask = models.StringField()
	pair_answer_mean = models.IntegerField()

    ##### 1 out of 5
	five_scarce1 = models.StringField()
	five_scarce2 = models.StringField()
	five_scarce3 = models.StringField()
	five_scarce4 = models.StringField()
	five_scarce5 = models.StringField()
	
	five_mask1 = models.StringField()
	five_mask2 = models.StringField()
	five_mask3 = models.StringField()
	five_mask4 = models.StringField()
	five_mask5 = models.StringField()

	five_mask1_value = models.IntegerField()
	five_mask2_value = models.IntegerField()
	five_mask3_value = models.IntegerField()
	five_mask4_value = models.IntegerField()
	five_mask5_value = models.IntegerField()

	five_scarce = models.StringField()
	five_scarce_answer_mask = models.StringField()
	five_scarce_answer_mean = models.FloatField()

	##### 3 out of 5 (Multiple_choice)
	five_multiple1 = models.StringField()
	five_multiple2 = models.StringField()
	five_multiple3 = models.StringField()
	five_multiple4 = models.StringField()
	five_multiple5 = models.StringField()

	five_m_mask1 = models.StringField()
	five_m_mask2 = models.StringField()
	five_m_mask3 = models.StringField()
	five_m_mask4 = models.StringField()
	five_m_mask5 = models.StringField()

	five_mc = tool_models.MultipleChoiceModelField(label="Please select the three correct statements",
                                                              min_choices=3, max_choices=3)
	
	five_m_mask1value = models.IntegerField()
	five_m_mask2value = models.IntegerField()
	five_m_mask3value = models.IntegerField()
	five_m_mask4value = models.IntegerField()
	five_m_mask5value = models.IntegerField()


	five_mc_mean1 = models.IntegerField()
	five_mc_mean2 = models.IntegerField()
	five_mc_mean3 = models.IntegerField()
	five_mc_mean4 = models.IntegerField()
	five_mc_mean5 = models.IntegerField()


	# Lottery
	lottery1_1 = models.BooleanField()
	lottery1_1_mask = models.StringField()
	lottery1_1_img = models.StringField()
	lottery1_1_value = models.IntegerField()

	lottery1_2 = models.BooleanField(blank = True)
	lottery1_2_mask = models.StringField()
	lottery1_2_img = models.StringField()
	lottery1_2_value = models.IntegerField()

	lottery1_3 = models.BooleanField(blank = True)
	lottery1_3_mask = models.StringField()
	lottery1_3_img = models.StringField()
	lottery1_3_value = models.IntegerField()

	lottery1_4 = models.BooleanField(blank = True)
	lottery1_4_mask = models.StringField()
	lottery1_4_img = models.StringField()
	lottery1_4_value = models.IntegerField()

	lottery1_5 = models.BooleanField(blank = True)
	lottery1_5_mask = models.StringField()
	lottery1_5_img = models.StringField()
	lottery1_5_value = models.IntegerField()

	lottery1_player = models.StringField(default = "")
	lottery1_mask = models.StringField(default = "")
	lottery1_value = models.IntegerField(default = None)

	rate_lottery1_2 = models.IntegerField(blank = True)
	rate_lottery1_3 = models.IntegerField(blank = True)	
	rate_lottery1_4 = models.IntegerField(blank = True)
	rate_lottery1_5 = models.IntegerField(blank = True)

	###### Demographics 
	age = models.IntegerField()

	#multiple_choice_five = tool_models.MultipleChoiceModelField(label="Please select the best three players for your team!",
    #                                                          min_choices=3, max_choices=3)

	def vars_for_template(self):
   		return{
    	"img_pair1_1": self.pairs1_1,
    	"img_pair1_2": self.pairs1_2,
    	"mask1_1": self.mask1_1,
    	"mask1_2": self.mask1_2,
    	'pair_answer': self.pair_answer,
    	'mask1_1_value': self.mask1_1_value,
    	'mask1_2_value': self.mask1_2_value,

    	"img_five_scarce1": self.five_scarce1,
    	"img_five_scarce2": self.five_scarce2,
    	"img_five_scarce3": self.five_scarce3,
    	"img_five_scarce4": self.five_scarce4,
    	"img_five_scarce5": self.five_scarce5,

    	"five_mask1": self.five_mask1, 
    	"five_mask2": self.five_mask2, 
    	"five_mask3": self.five_mask3, 
    	"five_mask4": self.five_mask4, 
    	"five_mask5": self.five_mask5, 

    	"five_mask1_value": self.five_mask1_value,
    	"five_mask2_value": self.five_mask2_value,
    	"five_mask3_value": self.five_mask3_value,
    	"five_mask4_value": self.five_mask4_value,
    	"five_mask5_value": self.five_mask5_value,

    	"img_five_multiple1": self.five_multiple1,
    	"img_five_multiple2": self.five_multiple2,
    	"img_five_multiple3": self.five_multiple3,
    	"img_five_multiple4": self.five_multiple4,
    	"img_five_multiple5": self.five_multiple5,

    	"five_m_mask1": self.five_m_mask1, 
    	"five_m_mask2": self.five_m_mask2,
    	"five_m_mask3": self.five_m_mask3,
    	"five_m_mask4": self.five_m_mask4,
    	"five_m_mask5": self.five_m_mask5,

    	'five_m_mask1value': self.five_m_mask1value, 
    	'five_m_mask2value': self.five_m_mask2value,
    	'five_m_mask3value': self.five_m_mask3value, 
    	'five_m_mask4value': self.five_m_mask4value, 
    	'five_m_mask5value': self.five_m_mask5value,

    	'lottery1_1_img': self.lottery1_1_img,
    	'lottery1_2_img': self.lottery1_2_img,
    	'lottery1_3_img': self.lottery1_3_img,
    	'lottery1_4_img': self.lottery1_4_img,
    	'lottery1_5_img': self.lottery1_5_img,

    	'lottery1_1_mask': self.lottery1_1_mask,
    	'lottery1_2_mask': self.lottery1_2_mask,
    	'lottery1_3_mask': self.lottery1_3_mask,
    	'lottery1_4_mask': self.lottery1_4_mask,
    	'lottery1_5_mask': self.lottery1_5_mask,

    	'lottery1_1_value': self.lottery1_1_value, 
    	'lottery1_2_value': self.lottery1_2_value,
    	'lottery1_3_value': self.lottery1_3_value,
    	'lottery1_4_value': self.lottery1_4_value,
    	'lottery1_5_value': self.lottery1_5_value,

    	'endowment1': self.endowment1, 
    	'endowment2': self.endowment2, 
    	'endowment3': self.endowment3, 
    	'endowment4': self.endowment4,

    	'endowment1mask': self.endowment1mask, 
    	'endowment2mask': self.endowment2mask,
    	'endowment3mask': self.endowment3mask,
    	'endowment4mask': self.endowment4mask,

    	'team_endowment': np.mean(list(filter(None, [self.endowment1value, self.endowment2value, self.endowment3value, self.endowment4value, self.pair_answer_mean, self.five_mc_mean1,
    		self.five_mc_mean2, self.five_mc_mean3, self.five_mc_mean4, self.five_mc_mean5, self.five_scarce_answer_mean, self.lottery1_value]))),
    	'team_endowment_cent': np.mean(list(filter(None, [self.endowment1value, self.endowment2value, self.endowment3value, self.endowment4value, self.pair_answer_mean, self.five_mc_mean1,
    		self.five_mc_mean2, self.five_mc_mean3, self.five_mc_mean4, self.five_mc_mean5, self.five_scarce_answer_mean, self.lottery1_value])))/100,
    	'probability': self.probability,

    	'success': np.random.binomial(1, np.mean(list(filter(None, [self.endowment1value, self.endowment2value, self.endowment3value, self.endowment4value, self.pair_answer_mean, self.five_mc_mean1,
    		self.five_mc_mean2, self.five_mc_mean3, self.five_mc_mean4, self.five_mc_mean5, self.five_scarce_answer_mean, self.lottery1_value])))/100, 1),

    	} 


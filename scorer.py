'''
author = Mitch Rule
email = mitchman5506@gmail.com

This program will keep score of a game of darts for two players.
Each player has to count their score down from 501 and reach zero on 
a double number.
Players will enter their throws into the terminal with a specific syntax
and the scorer calculate their score and eventually determine a winner.
'''
import re


class Player(object):
	'''
	Contains all of the data for each player
	and the functions for calculating scores.
	'''

	def __init__(self, name):
		self.name = name
		self.score = 501
		self.throws = []

	def throw(throws):
		pass


def scoreConvert(throws):
	'''
	Takes inputs as a list of three throws.
	Applies triple and double multipliers.
	
	Example: 'T20' --> 60
	'''
	convertedThrows = []

	for throw in throws:
		if 'd' in throw.lower():
			# Strips character from the start of string to get number only
			strippedThrow = re.sub(r'd', '', throw.lower())
			throw = int(strippedThrow) * 2
			convertedThrows.append(throw)

			print(strippedThrow)
			print('Double score')
		elif 't' in throw.lower():
			strippedThrow = re.sub(r't', '', throw.lower())
			throw = int(strippedThrow) * 3
			convertedThrows.append(throw)

			print(strippedThrow)
			print('Triple score')
		else:
			print('Single score')
			throw = int(throw)
			convertedThrows.append(throw)

	return convertedThrows
	print(convertedThrows)


#Test
scoreConvert(['T20', 'D20', '15'])
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
        self.throwlist = []


def scoreConvert(throws):
    '''
    Takes inputs as a list of three string throws.
    Applies triple and double multipliers.

    Returns throws as list of integers

    Example: ['T20', 'D20', '15'] --> [60, 40, 15]
    '''

    convertedThrows = []

    # TODO Add bullseye
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


def isValidThrow(throws):
    '''
    Takes throws and returns True or False to
    whether they are legal throws.

    Example: ['T21', '20', '20'] --> False
    '''

    valid = True
    validThrows = []

    for i in range(1, 21):
        validThrows.append(str(i))
        validThrows.append('d' + str(i))
        validThrows.append('t' + str(i))

    validThrows.append('25')
    validThrows.append('50')

    for throw in throws:
        if throw.lower() in validThrows:
            pass
        else:
            valid = False
            break

    return valid

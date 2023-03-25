

import random


def roll_dice(dices,random_number=0):

    '''Dice List that will be full later'''
    dice_list = []
    dies=dices
    random.seed(random_number)

    '''If more than 10 die or less than 1 die'''
    if dies < 1 and dies > 10:
        dice_list = [6]
    '''If between 1 and 10 die'''
    if dies > 0 and dies < 11:
        for i in range (dies+1):
            new_dice=random.randint(1,6)
            dice_list.append(new_dice)
    '''If nothing is input'''
    if dices == None and random_number == 0:
        for i in range (4):
            new_dice = random.randint(1, 6)
            dice_list.append(new_dice)
    return dice_list

def are_valid(rand_list):
    acceptable_die = [1,2,3,4,5,6]
    list_len = len(rand_list)
    counter_valid = 0

    '''Checks to see if the # of die are between 0~10'''
    if list_len > 0 and list_len < 10:
        for i in range(list_len):
            '''Checks to see if the die are between 1~6'''
            if list_len[i] in acceptable_die:
                counter_valid += 1

    if counter_valid == list_len:
        return True
    else:
        return False


def count_values(dies, check=None):
    counter_value = 0
    '''Counting occurrences'''
    for i in range (dies):
        if i == check:
            counter_value += 1

    if (dies < 1) or (dies > 10) or (check == None):
        return -1
    else:
        return counter_value

def add_values(dies_list):
    if dies_list > 0 and dies_list < 11:
        if are_valid(dies_list) == True:
            return sum(dies_list)
        if are_valid(dies_list) == False:
            return -1
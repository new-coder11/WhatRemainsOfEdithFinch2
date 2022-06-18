##imports
import time as tm

var = num = 0

def show_part(part):
    show_part_with_user(part, None)


def show_part_with_user(part, user):
    part_file = open('{}.txt'.format(part), 'r')
    all_lines = part_file.readlines()

    for line in all_lines:
        if len(line.strip()) > 0:
            tm.sleep(5)

        if line.__contains__('{}'):
            print(line.format(user))
        else:
            print(line)


show_part('intro_part1')

user = input('What name do you go by?')
print('Well ', user)
print('There is a lot of family history to get through, so lets get started')

show_part_with_user('intro_part2', user)
show_part_with_user('game_start', user)

doyou = input('Do you want to embark on this adventure? 1, yes  2, no')
if doyou == '1':
    print('Lets do this')
    show_part('game')
else:
    print('That is unfortunate, now you have to wait another fifty years')

book = input('Do you want to read the book? 1, yes  2, no')
if book == '1':
    print('You open the pages, of which are all stuck together due to the water')
    who = input('Who would you like to read about? 1 Ingeborg, 2 Johann, 3 Edie')
else:
    print('You start to explore the areas of the house')
    show_part('house')
    print('You pick up the book again')
    print('You open the pages, of which are all stuck together due to the water')
    who = input('Who would you like to read about? 1 Ingeborg, 2 Johann, 3 Edie')




while num < 4:
    num +=1
    if who == '1':
        show_part('ingeborg')
        who = input('Who would you like to read about? 1 Ingeborg, 2 Johann, 3 Edie, 4 to stop reading')
    elif who == '2':
        show_part('johann')
        who = input('Who would you like to read about? 1 Ingeborg, 2 Johann, 3 Edie, 4 to stop reading')
    elif who == '3':
        show_part('edie')
        who = input('Who would you like to read about? 1 Ingeborg, 2 Johann, 3 Edie, 4 to stop reading')
    elif who == '4':
        w = input('What do you want to do? 1 leave the house, 2 explore the house')
        if w == '1':
            show_part_with_user('leave', user)
            break
        elif w == '2':
            show_part('house')

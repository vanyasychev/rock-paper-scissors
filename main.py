import random


def winner(user, computer):
    global glasses

    if computer in user_option.get(user):
        glasses += 100
        return f'Well done. The computer chose {computer} and failed'
    elif user in user_option.get(computer):
        return f'Sorry, but the computer chose {computer}'
    else:
        glasses += 50
        return f'There is a draw ({computer})'


def input_validation():
    while True:
        string = input()

        if string in list(user_option) or string in ('!exit', '!rating'):
            return string
        else:
            print('Invalid input')


def scoring():
    global glasses

    with open('rating.txt') as f:
        output = [j.replace('\n', '') for j in f]

        for j in output:
            if user_name in j[:len(user_name)]:
                glasses = int(j.split()[1])
                return glasses
            return 0


regulations = {'rock': ('fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'),
               'fire': ('scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'),
               'scissors': ('snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'),
               'snake': ('human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'),
               'human': ('tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'),
               'tree': ('wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'),
               'wolf': ('sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'),
               'sponge': ('paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'),
               'paper': ('air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'),
               'air': ('water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'),
               'water': ('dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'),
               'dragon': ('devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'),
               'devil': ('lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'),
               'lightning': ('gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'),
               'gun': ('rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf')}

user_name = input('Enter your name: ')
print('Hello,', user_name)
glasses = scoring()

option_list = input().replace(',', ' ').split()
print("Okay, let's start")

user_option = dict()
if len(option_list) != 0:
    for i in option_list:
        if i in regulations:
            user_option[i] = tuple(set(option_list) & set(regulations[i]))
else:
    user_option = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

while True:
    user_chose = input_validation()

    if user_chose == '!rating':
        print('Your rating:', glasses)
    elif user_chose != '!exit':
        computer_chose = random.choice(list(user_option))
        print(winner(user_chose, computer_chose) if user_chose != 'exit' else 'Bye!')
    else:
        break

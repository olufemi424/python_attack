# variable
# player_name = 'Olufemi'
# player_attack = 10
# player_heal = 16
# health = 100

# List
# player = ['Olufemi', 10, 16, 100]


game_running = True

while game_running == True:

    new_round = True
    # Dictionary
    player = {
        'name': 'Olufemi',
        'attack': 13,
        'heal': 16,
        'health': 100
    }

    monster = {
        'name': 'Max',
        'attack': 12,
        'health': 100
    }

    while new_round == True:

        print('Pls select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')

        player_won = False
        monster_won = False

        player_choice = input()
        print(player['name'])

        # if statement
        if player_choice == 1:
            monster['health'] = monster['health'] - player['attack']

            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - monster['attack']

                if player['health'] <= 0:
                    monster_won = True

            player['health'] = player['health'] - monster['attack']
            print(monster['health'])
            print(player['health'])

        elif player_choice == 2:
            print('Heal')

        elif player_choice == 3:
            new_round = False
            game_running = False
            print('Game Exit')

        else:
            print('Input is not an option')

        if player_won == True or monster_won == True:
            new_round = False

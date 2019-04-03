from random import randint

# variable
# player_name = 'Olufemi'
# player_attack = 10
# player_heal = 16
# health = 100

# List
# player = ['Olufemi', 10, 16, 100]

# init game start
game_running = True

# while game is running
while game_running == True:

   # create plater and monster with their details

   #  Init new round
    new_round = True
    # Dictionary

   #  player details
    player = {
        'name': 'Olufemi',
        'attack': 13,
        'heal': 16,
        'health': 100
    }

   # monster details
    monster = {
        'name': 'Max',
        'attack_min': 10,
        'attack_max': 20,
        'health': 100
    }

   # get player name
    print('---' * 7)
    print('Enter player name')
    player['name'] = input()

   # display player and monster info
    print('---' * 7)
    print(player['name'] + ' has ' + str(player['health']) + ' health.')
    print(monster['name'] + ' monster has ' +
          str(monster['health']) + ' health.')

   # always start a new round if the player doesnt quit
    while new_round == True:

      #  init wining status
        player_won = False
        monster_won = False

      # print player choice
        print('---' * 7)
        print('Pls select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')

      # get player choice
        player_choice = input()
        print(player['name'])

        # check player choice
        if player_choice == '1':
            monster_attack = randint(
                monster['attack_min'], monster['attack_max'])

            monster['health'] = monster['health'] - player['attack']
            # check monster health to determine if game player has won
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - monster_attack

                if player['health'] <= 0:
                    monster_won = True

        elif player_choice == '2':
            monster_attack = randint(
                monster['attack_min'], monster['attack_max'])
            player['health'] = player['health'] + player['heal']

            player['health'] = player['health'] - monster_attack
            if player['health'] <= 0:
                monster_won = True

        elif player_choice == '3':
            new_round = False
            game_running = False
            print('Game Exit')

        else:
            print('Input is not an option')

        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' +
                  str(player['health']) + ' health left.')
            print(monster['name'] + ' has ' +
                  str(monster['health']) + ' health left.')

        elif player_won:
            print(player['name'] + ' won ')
            new_round = False

        if monster_won:
            print('The Monster won')
            new_round = False

            # print(monster['health'])
            # print(player['health'])

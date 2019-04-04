from random import randint

# init game start
game_running = True
game_results = []


def calculate_monster_attack():  # create a random monster attack
    return randint(monster['attack_min'], monster['attack_max'])


def game_ends(winner_name):  # print winner function
    print(f'{winner_name} Won The Game')


# while game is running
while game_running == True:

    # create plater and monster with their details
    counter = 0
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

        counter = counter + 1
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
            monster_attack = calculate_monster_attack()  # monster attack function

            # eack attack is fired both ways, the player get hit, and monster get hit
            # and check if the moster is still with health or deal, the player get hit each time an attacl is fired as long as the monster is still alive
            monster['health'] = monster['health'] - player['attack']
            # check monster health to determine if player has won
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - monster_attack

                if player['health'] <= 0:
                    monster_won = True

      # heal choice
        elif player_choice == '2':
            monster_attack = calculate_monster_attack()  # monster attack function

         # increase player health with player heal value
            player['health'] = player['health'] + player['heal']
         # there is also a hit from the monster and check if player still got health
            player['health'] = player['health'] - monster_attack
            if player['health'] <= 0:
                monster_won = True
         # choice 3
         # quit the game
        elif player_choice == '3':
            new_round = False
            game_running = False
            print('Game Exit')

      #  choice not an option
        else:
            print('Input is not an option')

        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' +
                  str(player['health']) + ' health left.')
            print(monster['name'] + ' has ' +
                  str(monster['health']) + ' health left.')

        elif player_won:
            game_ends(player['name'])
            round_result = {
                'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            print(game_results)
            new_round = False

        if monster_won:
            game_ends(monster['name'])
            round_result = {
                'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            print(game_results)
            new_round = False

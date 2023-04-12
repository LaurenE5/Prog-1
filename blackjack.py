from p1_random import P1Random
rng = P1Random()

blackjack = True
# Counters throughout game
game_count = 0
player_wins = 0
dealer_wins = 0
tie_games = 0

# Option Menu
blackjack_menu = """
1. Get another card
2. Hold hand
3. Print statistics
4. Exit
"""

while blackjack:
    # beginning script
    card = rng.next_int(13) + 1
    game_count += 1
    print('\n')
    print('START GAME #', game_count)
    player_hand = 0

    # Card Values
    if card == 1:
        print('Your card is a ACE!')
        player_hand += 1
    elif card == 11:
        print('Your card is a JACK!')
        player_hand += 10
    elif card == 12:
        print('Your card is a QUEEN!')
        player_hand += 10
    elif card == 13:
        print('Your card is a KING!')
        player_hand += 10
    else:
        print(f'Your card is a {card}!')
        player_hand += card

    print('Your hand is:', player_hand)

    # While loop for individual games
    while True:
        print(blackjack_menu)
        player_choice = int(input('Choose an option: '))

        # Drew another card
        if player_choice == 1:
            card = rng.next_int(13) + 1

            # Card Values (again)
            if card == 1:
                print('Your card is a ACE!')
                player_hand += 1
            elif card == 11:
                print('Your card is a JACK!')
                player_hand += 10
            elif card == 12:
                print('Your card is a QUEEN!')
                player_hand += 10
            elif card == 13:
                print('Your card is a KING!')
                player_hand += 10
            else:
                print(f'Your card is a {card}!')
                player_hand += card

            print('Your hand is:', player_hand)

            # Game ending (Not on purpose -> get over 21, or get 21 exactly)
            if player_hand > 21:
                print('You exceeded 21! You lose.')
                dealer_wins += 1
                break
            elif player_hand == 21:
                print('BLACKJACK! You win!')
                player_wins += 1
                break

        # Ended game on purpose
        elif player_choice == 2:
            dealer_hand = rng.next_int(11) + 16
            print('Dealer\'s hand:', dealer_hand)
            print('Your hand is:', player_hand)
            if dealer_hand > 21 or player_hand > dealer_hand:
                print('You win!')
                player_wins += 1
                break
            elif dealer_hand > player_hand:
                print('Dealer wins!')
                dealer_wins += 1
                break
            else:
                print('It\'s a tie! No one wins!')
                tie_games += 1
                break

        # Statistics of all games
        elif player_choice == 3:
            print('Number of Player wins: ', player_wins)
            print('Number of Dealer wins: ', dealer_wins)
            print('Number of tie games: ', tie_games)
            print('Total # of games played is: ', (player_wins + dealer_wins + tie_games))
            player_win_percentage = float(player_wins / (player_wins + dealer_wins + tie_games))
            print(f'Percentage of Player wins: {(player_win_percentage * 100):.1f}', end='%')
            print('\n')
            continue

        # Exiting program
        elif player_choice == 4:
            blackjack = False
            break

        # Didn't select an option
        else:
            print('Invalid input!\nPlease enter an integer value between 1 and 4.')
            continue

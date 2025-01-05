import random
from art import bj_logo


def clear_screen():
    print("\n" * 100)


def pause():
    input("Press enter to continue: ")


want_to_play = input("Down for some Blackjack? Type 'y' or 'n': ").lower()

while want_to_play != 'y' or want_to_play != 'n':
    if want_to_play == 'y':
        print(bj_logo)
        print("""############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Ace can count as 11 or 1.
## the following list is the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The Jack/Queen/King all count as 10.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer. 

        """)
        break
    elif want_to_play == 'n':
        print("Aww man :(")
        exit()
    else:
        want_to_play = input("Please enter a valid option. Type 'y' or 'n': ")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    """Determines the initial draw of cards for the user and the dealer."""
    user_cards = random.sample(cards, 2)
    dealer_cards = random.sample(cards, 2)
    print(f"Your cards: {user_cards}, current total: {sum(user_cards)}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    def decisions():
        """Progresses through the game based on whether the user chooses to hit or stand."""
        nonlocal dealer_cards, user_cards

        if sum(user_cards) == 21:
            print("We have a Blackjack!")

        hit_or_stand = input("Please type 'hit' to hit, type 'stand' to stand: ").lower()
        clear_screen()
        while hit_or_stand == 'hit':
            user_new_card = random.choice(cards)
            user_cards.append(user_new_card)
            print(f"You drew {user_new_card}. Your cards are now {user_cards}, and your total is: {sum(user_cards)}.")
            # Checks if user has an Ace and converts it from 11 to 1.
            if sum(user_cards) > 21 and 11 in user_cards:
                user_cards[user_cards.index(11)] = 1
                print(f"Since you drew an Ace (11/1), and you went over 21, your total is now: {sum(user_cards)}")
                print(f"Your cards are: {user_cards}")
            if sum(user_cards) > 21:
                print("Bust. You lose! ")
                pause()
                break
            elif sum(user_cards) == 21:
                print("We have a Blackjack! ")
                pause()
                break
            else:
                hit_or_stand = input("Please type 'hit' to hit, type 'stand' to stand: ").lower()
                clear_screen()

        if hit_or_stand == 'stand':
            print(f"The dealer's cards were {dealer_cards}. The dealer's total is {sum(dealer_cards)}")
            pause()
        elif hit_or_stand == 'hit':
            print(f"The dealer's cards were {dealer_cards}. The dealer's total is {sum(dealer_cards)}")
            pause()
        else:
            print("Invalid input. \n")
            decisions()

    def end_game():
        """Finishes the game off and determines the outcome based on win conditions."""
        nonlocal dealer_cards, user_cards

        while sum(dealer_cards) < 17:
            dealer_new_card = random.choice(cards)
            dealer_cards.append(dealer_new_card)
            print(f"The dealer drew {dealer_new_card} and now has {dealer_cards}. Their total is: {sum(dealer_cards)}")
            pause()
            if sum(dealer_cards) > 21 and 11 in dealer_cards:
                dealer_cards[dealer_cards.index(11)] = 1
                print(f"Since the dealer drew an Ace (11/1) and went over 21, their total is now: {sum(dealer_cards)}")
                print(f"dealers cards are: {dealer_cards}")
                pause()
        # WIN CONDITIONS GO HERE:
        if sum(dealer_cards) > 21:
            print("Dealer busts! ")
            if sum(user_cards) <= 21:
                print("You win by dealer bust! ")
            else:
                print("You and the dealer both went bust and lose! ")
        elif sum(dealer_cards) <= 21 < sum(user_cards):
            print("Dealer wins by player bust! ")
        elif sum(dealer_cards) <= 21 and sum(user_cards) <= 21:
            if sum(dealer_cards) > sum(user_cards):
                print("Dealer wins by amount! ")
            elif sum(user_cards) > sum(dealer_cards):
                print("You win by amount! ")
            else:
                print("Push! You and the dealer had a draw.")
        restart = ' '
        while restart != 'y' or restart != 'n':
            restart = input("Would you like to play again? Type 'y' or 'n': ")
            if restart == 'y':
                clear_screen()
                game = blackjack()
                game[0]()
                game[1]()
                blackjack()
            elif restart == 'n':
                clear_screen()
                print("Hope you had fun! Goodbye!")
                exit()
            else:
                print("Invalid input. \n")
                continue

    return decisions, end_game


decisions_func, end_game_func = blackjack()

decisions_func()
end_game_func()

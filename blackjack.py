from art import logo

import random


def deal_card():
    """Deal one random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards_in_hand):
    """Calculate the score of the available cards in hand."""
    if len(cards_in_hand) == 2 and 11 in cards_in_hand and 10 in cards_in_hand:
        return 0
    if sum(cards_in_hand) > 21 and 11 in cards_in_hand:
        cards_in_hand.remove(11)
        cards_in_hand.append(1)
    return sum(cards_in_hand)


def compare(usr_score, com_score):
    """Compare the scores between user and computer to give the result."""
    if usr_score > 21:
        print("You lose!")
    elif com_score > 21:
        print("You win!")
    else:
        if usr_score == 0:
            print("You win! Blackjack!")
        elif com_score == 0:
            print("You lose! Computer Blackjack!")

        if usr_score > com_score:
            print("You win!")
        elif usr_score < com_score:
            print("You lose!")
        elif usr_score == com_score:
            print("It's a draw!")


end_game = False
while not end_game:
    # Initial cards
    user_cards = []
    computer_cards = []
    deal_flag = True

    want_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_play == 'y':
        print(logo)
        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        user_score = calculate_score(cards_in_hand=user_cards)
        computer_score = calculate_score(cards_in_hand=computer_cards)

        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"\tComputer's first card: {computer_cards}, current score: {computer_score}")

        if user_score == 0 or computer_score == 0:
            print(f"\tYour final hand: {user_cards}, final score: {user_score}")
            print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
            if user_score == computer_score:
                print("You both have blackjack!")
            elif user_score == 0:
                print("You win! Blackjack!")
            elif computer_score == 0:
                print("You lose! Computer Blackjack!")
            continue

        # User play
        while deal_flag:
            want_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if want_deal == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(cards_in_hand=user_cards)
                if user_score > 21:
                    deal_flag = False
                    # end_game = True
                print(f"\tYour cards: {user_cards}, current score: {user_score}")
                print(f"\tComputer's first hand: {computer_cards}, final score: {computer_score}")
            elif want_deal == 'n':
                deal_flag = False

        # Computer play
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(cards_in_hand=computer_cards)

        print(f"\tYour final hand: {user_cards}, final score: {user_score}")
        print(f"\tComputer's final card: {computer_cards}, current score: {computer_score}")

        compare(usr_score=user_score, com_score=computer_score)

    elif want_play == 'n':
        end_game = True


#!/usr/bin/env python3
import cards
import db
import locale as lc

result = lc.setlocale(lc.LC_ALL, "")
if result == "C":
    lc.setlocale(lc.LC_ALL, "en_US")


def display_title():
    # print the header
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print("Enter \'x\' for bet to exit")
    print()


def get_starting_money():
    try:
        money = db.read_money()
    except FileNotFoundError:
        print("Data file missing, resetting starting amount to 1000.")
        money = 1000

    if money < 5:
        print("You were out of money")
        print("We gave you 100 so you could play.")
        db.write_money(100)
        return 100
    else:
        return money


def get_bet(money):
    while True:
        try:
            bet = float(input("Bet amount:      "))
        except ValueError:
            print("Invalid amount. Try again.")
            continue


        bet = float(bet)
        if bet < 5:
            print("The minimum bet is 5.")
        elif bet > 1000:
            print("The maximum bet is 1,000")
        elif bet > money:
            print("You don't have enough money to make that bet.")
        else:
            return bet



def display_cards(hand, title):
    print(title.upper())
    for card in hand:
        print(card[0], "of", card[1])
    print()


def play(deck, player_hand):
    while True:
        choice = input("Hit or stand? (h/s): ")
        print()

        if choice.lower() == "h":
            cards.add_card(player_hand, cards.deal_card(deck))
            if cards.get_points(player_hand) > 21:
                display_cards(player_hand, "YOUR CARDS: ")
                break
            display_cards(player_hand, "YOUR CARDS: ")
        elif choice.lower() == "s":
            break
        else:
            print("Not a valid choice, Try again.")

    return player_hand

def buy_more_chips(money):
    while True:
        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("Invalid amount. Try again.")
            continue
        if 0 < amount <= 10000:
            money += amount
            return money
        else:
            print("Invalid amount, must be from 0 to 10,000.")



def main():
    display_title()

    # read the money and bet values from the user
    money = get_starting_money()
    print("Money:", lc.currency(money, grouping=True))
    print()

    while True:
        if money < 5:
            print("You are out of money.")
            buy_more = input("Would you like to buy more chips? (y/n): ").lower()
            if buy_more == "y":
                money = buy_more_chips(money)
                print("Money: ", lc.currency(money, grouping=True))
                db.write_money(money)
            else:
                break

        bet = get_bet(money)
        if bet == "x":
            break
        print()

        deck = cards.get_deck()
        cards.shuffle(deck)

        dealer_hand = cards.get_empty_hand()
        player_hand = cards.get_empty_hand()

        cards.add_card(player_hand, cards.deal_card(deck))
        cards.add_card(player_hand, cards.deal_card(deck))
        cards.add_card(dealer_hand, cards.deal_card(deck))

        display_cards(dealer_hand, "DEALER'S SHOW CARD: ")
        display_cards(player_hand, "YOUR CARDS: ")

        player_hand = play(deck, player_hand)

        while cards.get_points(dealer_hand) < 17:
            cards.add_card(dealer_hand, cards.deal_card(deck))
        display_cards(dealer_hand, "DEALER'S CARDS: ")

        print("YOUR POINTS:       " + str(cards.get_points(player_hand)))
        print("DEALER'S POINTS:   " + str(cards.get_points(dealer_hand)))
        print()

        players_points = cards.get_points(player_hand)
        dealer_points = cards.get_points(dealer_hand)

        if players_points > 21:
            print("Sorry, you busted. You lose.")
            money -= bet
        elif dealer_points > 21:
            print("Yay! Dealer busted. You win!")
            money += bet
        else:
            if players_points == 21 and len(player_hand) == 2:
                if dealer_points == 21 and len(dealer_hand) == 2:
                    print("Dang, dealer has blackjack too. You push")
                else:
                    print("Blackjack! You win!")
                    money += bet * 1.5
                    money = round(money, 2)
            elif players_points > dealer_points:
                print("Hooray! You win!")
                money += bet
            elif dealer_points > players_points:
                print("Sorry, You lose.")
                money -= bet
            elif players_points == dealer_points:
                print("You push.")
            else:
                print("Sorry, I am not sure what happened.")

        print("Money", lc.currency(money, grouping=True))

        db.write_money(money)
        print()
        again = input("Play again? (y/n): ")
        print()
        if again.lower() != "y":
            print("Come again soon!")
            break

        print()

    #exit
    print("Bye!")

if __name__ == "__main__":
    main()



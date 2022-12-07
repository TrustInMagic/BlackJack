from deck import Deck
import card_sintax

class Blackjack:
    def __init__(self):
        self.player_money = 500
        self.bet = 0

    def start(self):
        print("Welcome to Blackjack! \n")
        self.pre_game()

    def pre_game(self):
        if self.player_money > 0:
            player_accept = input(f"You are starting with ${self.player_money}. Would you like to play a hand? ")

            if player_accept.lower() == "yes":
                self.betting_round()
            else:
                self.end_game()
                
    
    def betting_round(self):
        while True:
            bet = int(input("Place your bet: "))

            if bet < 1:
                print("The minimum bet is $1.")
            elif bet > self.player_money:
                print("You do not have sufficient funds.")
            else:
                self.bet = bet
                self.actual_game()
                break
                

    def actual_game(self):
        d = Deck()
        d.shuffle_deck()

        dealer_hand = d.deal_cards(2)
        player_hand = d.deal_cards(2)
        player_points = card_sintax.blackjack_value(player_hand)
        aces = []
        

        print(f"You are dealt: {player_hand[0]}, {player_hand[1]}")
        print(f"The dealer is dealt: {dealer_hand[0]}, Unknown")


        if self.blackjack_checker(player_hand) == True and self.blackjack_checker(dealer_hand) == False:
            print(f"Blackjack! You win ${round(self.bet * 1.5)} :)")
            print(f"Dealer has: {dealer_hand[0]}, {dealer_hand[1]}")
            self.player_money += round(self.bet * 1.5)
            self.pre_game()

        
        while player_points <= 21:
            decision = card_sintax.hit_or_stay()

            if decision == "hit":
                hit = d.deal_cards(1)
                print(f"You are dealt: {hit[0]}")
                player_hand.append(hit[0])
                print(card_sintax.hand_displayer(player_hand, aces))
                player_points = card_sintax.blackjack_value(player_hand)

            else:
                self.showdown(dealer_hand, player_hand, d)
                break
            

            while player_points > 21:
                card_sintax.ace_swapper(player_hand, aces)
                player_points = card_sintax.blackjack_value(player_hand)


            if player_points > 21:
                print(f"Your hand value is over 21 and you lose ${self.bet} :(")
                self.player_money -= self.bet
                self.pre_game()


    def showdown(self, dealers_hand, player_hand, deck):
        dealer_hand = dealers_hand[:]
        dealer_points = card_sintax.blackjack_value(dealer_hand)
        aces = []
        hand_ender = 0

        print(f"The dealer has {dealer_hand[0]} {dealer_hand[1]}")

        if dealer_points > 21:
            card_sintax.ace_swapper(dealer_hand, aces)
            dealer_points = card_sintax.blackjack_value(dealer_hand)


        while dealer_points < 17:
            hit = deck.deal_cards(1)
            print(f"The dealer hits and is dealt: {hit[0]}")
            dealer_hand.append(hit[0])
            print(card_sintax.hand_displayer(dealer_hand, aces))
            dealer_points = card_sintax.blackjack_value(dealer_hand)

            while dealer_points > 21:
                card_sintax.ace_swapper(dealer_hand, aces)
                dealer_points = card_sintax.blackjack_value(dealer_hand)

            if dealer_points > 21:
                print(f"The dealer busts, you win ${self.bet}")
                hand_ender += 1
                self.player_money += self.bet
                self.pre_game()
                break
        
        if hand_ender == 0:
            print("The dealer stays.") 

            player_points = card_sintax.blackjack_value(player_hand)
        
            if player_points > dealer_points:
                print(f"You win ${self.bet}!")
                self.player_money += self.bet
            elif player_points < dealer_points:
                print(f"The dealer wins, you loose ${self.bet} :(")
                self.player_money -= self.bet
                if self.player_money == 0:
                    self.end_game()
            elif player_points == dealer_points:
                print(f"You tie. Your bet has been returned.")

            self.pre_game()


    def end_game(self):
        if self.player_money > 0:
            print(f"You left the table with ${self.player_money}. See you next time!")

        elif self.player_money == 0:
            print("You've ran out of money. Better luck next time!")
            

    @staticmethod
    def blackjack_checker(hand):
        if card_sintax.blackjack_value(hand) == 21:
            return True
        else:
            return False


b = Blackjack()

b.start()
def valid_cards():
    valid_numbers = [str(i) for i in range(2, 10)] + ["T", "J", "Q", "K", "A"]
    valid_suits = [u"\u2666", u"\u2665", u"\u2663",u"\u2660"]
    valid_cards = [number + suit for number in valid_numbers for suit in valid_suits]
    return valid_cards

def blackjack_value(cards):
    values = 0
    for card in cards:
        if "A" in card:
            values += 11
        if "1" in card:
            values += 1
        if "2" in card:
            values += 2
        elif "3" in card:
            values += 3
        elif "4" in card:
            values += 4
        elif "5" in card:
            values += 5
        elif "6" in card:
            values += 6
        elif "7" in card:
            values +=7
        elif "8" in card:
            values += 8
        elif "9" in card:
            values += 9
        elif "T" in card or "J" in card or "Q" in card or "K" in card:
            values += 10

    return values


def ace_swapper(cards):
    for idx, card in enumerate(cards):
        if "A" in card:
            cards[idx] = "1"
           
        

def hit_or_stay():
    while True:
        decision = input("Would you like to hit or stay? ")
        if decision == "hit" or decision == "stay":
            return decision     
        print("That is not a valid option.")



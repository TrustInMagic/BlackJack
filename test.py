hand = ["1" + u"\u2666", "Kd", "1" + u"\u2665", "6s"]
aces = ["A" + u"\u2666", "A" + u"\u2665"]

print(hand)
print(aces)

def hand_displayer(hand, aces):
    interior_hand = hand
    interior_aces = aces

    for idx, ace in enumerate(interior_aces):
        for idx2, card in enumerate(interior_hand):
            if card[0] == "1" and ace[1] == card[1]:
                interior_hand[idx2] = interior_aces[idx]
    
    return ", ".join(interior_hand)

            
print(hand_displayer(hand, aces))


deck_of_cards = input().split()
shuffles = int(input())

for cards in range(shuffles):
    shuffled_deck = []
    middle = len(deck_of_cards) // 2
    left_deck = deck_of_cards[0:middle]
    right_deck = deck_of_cards[middle::]
    for index_of_the_card in range(len(left_deck)):
        shuffled_deck.append(left_deck[index_of_the_card])
        shuffled_deck.append(right_deck[index_of_the_card])
    deck_of_cards = shuffled_deck
print(deck_of_cards)

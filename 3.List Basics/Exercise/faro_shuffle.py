deck_of_cards = input().split(',')
shuffles = int(input())

for cards in range(shuffles):
    shuffled_deck = []
    middle = len(deck_of_cards) // 2
    
import random

coin = ["Heads", "Tails"]
cards = ["Ace", "King", "Queen", "Jack"]


def main():
    # Random choice
    toss = random.choice(coin)
    print(toss)

    # it's a possibility that the output will give you ["queen","queen"]
    choices = random.choices(cards, k=2)
    print(choices)

    # If you don't want duplicates, use random.sample()
    samples = random.sample(cards, k=2)
    print(samples)

    # You can gamble things with adjusting the probability with weights
    gamble = random.choices(cards, weights=[50, 50, 0, 0], k=2)
    print(gamble)

    # If you want constant values , you can use random.seed()
    random.seed(1)
    constant = random.choices(cards, k=2)
    print(constant)

    # Random number
    number = random.randint(1, 10)
    print(number)

    # Shuffling the cards
    card = random.shuffle(cards)
    print(cards)
    # for card in cards:
    #     print(card)


if __name__ == "__main__":
    main()

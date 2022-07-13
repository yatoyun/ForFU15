import random
from unicodedata import name


def main():
    # ask name
    print("Who are you?")
    name = input(">")
    print(f"Hello, {name}!")

    # play the game : Heads or Tails
    print("Tossing a coin...")
    heads = tails = 0
    for i in range(5):
        if random.randint(0, 1) == 1:
            result = "Heads"
            heads += 1
        else:
            result = "Tails"
            tails += 1

        print(f"Round {i+1}: {result}")

    print(f"Heads: {heads}, tails: {tails}")
    if heads > tails:
        result = "won"
    else:
        result = "lost"
    print(f"{name} {result}!")


if __name__ == "__main__":
    main()

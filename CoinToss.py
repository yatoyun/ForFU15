import random


def main():
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


if __name__ == "__main__":
    main()
